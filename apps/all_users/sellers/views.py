from django.contrib.auth import get_user_model
from django.http import Http404

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.all_users.sellers.models import SellerModel
from apps.all_users.sellers.serializers import SellerSerializer
from apps.all_users.users.models import UserModel as User
from apps.all_users.users.serializers import UserSerializer
from apps.cars_details.cars.models import CarModelV2
from apps.cars_details.cars.serializers import CarSerializer

UserModel: User = get_user_model().objects.all()


class SellerListView(ListAPIView):
    queryset = UserModel.filter(roles='seller')
    serializer_class = UserSerializer


class SellerListByIdView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.filter(roles='seller')
    serializer_class = UserSerializer


class SellerCarsListCreateView(ListAPIView):
    queryset = UserModel.filter(roles='seller')
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        exist = UserModel.filter(pk=pk).exists()
        if not exist:
            raise Http404()
        cars = CarModelV2.objects.filter(seller_id=pk)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return (AllowAny(),)
    #     return (IsAuthenticated(),)

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        seller_id = UserModel.filter(roles='seller').first().id
        if seller_id:
            has_car = CarModelV2.objects.filter(seller_id=pk).exists()
            if not has_car:
                pk = kwargs['pk']
                data = self.request.data
                serializer = CarSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                exists = UserModel.filter(pk=pk).exists()
                if not exists:
                    raise Http404()
                serializer.save(seller_id=pk)
                # serializer.create_car(seller_id=pk)
                return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(
            'You cannot post more than one car, get more optionals https://example.com/info',status=status.HTTP_403_FORBIDDEN)

        # else:
        #     payment_url = 'your payment url here'
        #     return redirect(payment_url)

        # @api_view(['POST'])
    # @permission_classes(['isAuthenticated'])
    # def post(self, request, seller_id,  *args, **kwargs):  # add_car
    #     pk = kwargs['pk']
    #     existing_cars = CarModel.objects.filter(seller_id=pk)#(seller_id=seller_id)
    #     if existing_cars.exists():
    #         return Response('You can add only one car', status.HTTP_403_FORBIDDEN)
    #     else:
    #         serializer = CarSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save(seller_id=pk)
    #         return Response(serializer.data, status.HTTP_201_CREATED)
    #         # return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # def post(self, *args, **kwargs):  # написати катомну помилку що клієнт може створювати лише одну машину
    #     pk = kwargs['pk']
    #     data = self.request.data
    #     serializer = CarSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     exists = UserModel.filter(pk=pk).exists()
    #     if not exists:
    #         raise Http404()
    #     serializer.create(seller_id)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def post(self, request, *args, **kwargs):
    #     pk = kwargs['pk']
    #     seller_id = request.data.get('seller_id')
    #     max_cars_allowed = 1
    #     if CarModel.objects.filter(seller_id=seller_id).count() >= max_cars_allowed:
    #         return Response('You reached the max limit for creating cars', status=status.HTTP_403_FORBIDDEN)
    #     serializer = CarSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ChangeSellerToPremiumSellerView(APIView):
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        # seller = kwargs['pk']
        # user = UserModel.objects.get(pk=seller)
        # user.roles = 'premium_seller'
        # # # user.roles.premium_seller = True
        # serializer = UserSerializer(user)
        # # print(user)
        # user.save()
        # # return Response(serializer.data, status=status.HTTP_200_OK)
        # # else Response({'message':'error':'You are not authorized to perform this action'}, status=status.403_FORBIDDEN)
        user = get_object_or_404(UserModel, id=kwargs['pk'], roles='seller')
        user.roles = 'premium_seller'
        serializer = UserSerializer(user)
        user.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
