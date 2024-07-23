

from django.contrib.auth import get_user_model
from django.http import Http404

from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.all_users.premium_sellers.models import PremiumSellerModel
from apps.all_users.premium_sellers.serializers import PremiumSellerSerializer
from apps.all_users.users.models import UserModel as User
from apps.all_users.users.serializers import UserSerializer
from apps.cars_details.cars.models import CarModelV2
from apps.cars_details.cars.serializers import PremiumSellersCarsSerializer

# # from django.http import Http404
# # from rest_framework import status
# from django.http import Http404
# 
# from rest_framework import status
# from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# # from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# 
# from apps.cars_details.cars.models import CarModel
# from apps.cars_details.cars.serializers import CarSerializer
# 
# from .models import PremiumSellerModel
# # from rest_framework.response import Response
# # from rest_framework.mixins import ListModelMixin, CreateModelMixin
# from .serializers import PremiumSellerAllSerializer, PremiumSellerSerializer
# 
# 
# # class PremiumSellersListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
# # class PremiumSellersListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
# class PremiumSellersListCreateView(ListCreateAPIView):
#     serializer_class = PremiumSellerAllSerializer
#     # queryset = PremiumSellerModel.objects.all()
#     queryset = PremiumSellerModel.objects.prefetch_related('cars')
#     # permission_classes = (IsAuthenticated,)
#     # pagination_class = None
# 
#     # def get(self, request, *args, **kwargs):
#     #     return super().list(request, *args, **kwargs)
#     #
#     # def post(self, request, *args, **kwargs):
#     #     return super().create(request, *args, **kwargs)
# 
#     # def get(self, *args, **kwargs):
#     #     query_set = PremiumSellerModel.objects.all()
#     #     serializer = PremiumSellerSerializer(query_set, many=True)
#     #     return Response(serializer.data, status.HTTP_200_OK)
# 
#     # def post(self, *args, **kwargs):
#     #     data = self.request.data
#     #     serializer = PremiumSellerSerializer(data=data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#     #     return Response(serializer.data, status.HTTP_201_CREATED)
# 
# 
# class PremiumSellerUpdateRetrieveDestroyListView(RetrieveUpdateDestroyAPIView):
#     serializer_class = PremiumSellerSerializer
#     queryset = PremiumSellerModel.objects.all()
# 
#     # class PremiumSellerCarsListCreateView(GenericAPIView):
#     #     serializer_class = PremiumSellerSerializer
#     #     queryset = PremiumSellerModel.objects.all()
#     #
#     #     def get(self, *args, **kwargs):
#     #         pk = kwargs['pk']
#     #         exist = PremiumSellerModel.objects.filter(pk=pk).exists()
#     #         if not exist:
#     #             raise Http404()
#     #         cars = CarModel.objects.filter(premium_seller_id=pk)
#     #         serializer = CarSerializer(cars, many=True)
#     #         return Response(serializer.data, status.HTTP_200_OK)
#     #
#     #     def post(self, *args, **kwargs):
#     #         pk = kwargs['pk']
#     #         data = self.request.data
#     #         serializer = CarSerializer(data=data)
#     #         serializer.is_valid(raise_exception=True)
#     #         exists = PremiumSellerModel.objects.filter(pk=pk).exists()
#     #         if not exists:
#     #             raise Http404()
#     #         serializer.save(premium_seller_id=pk)
#     #         return Response(serializer.data, status.HTTP_201_CREATED)
# 
# 
# class PremiumSellerCarsListCreateView(GenericAPIView):
#     # serializer_class = PremiumSellerSerializer
#     queryset = PremiumSellerModel.objects.all()
# 
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
# 
#         exists = PremiumSellerModel.objects.filter(pk=pk).exists()
#         if not exists:
#             raise Http404()
# 
#         cars = CarModel.objects.filter(premium_seller_id=pk)
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
# 
#     def post(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         # premium_seller = self.get_object()
#         exists = PremiumSellerModel.objects.filter(pk=pk).exists()
#         if not exists:
#             raise Http404()
#         serializer.save(premium_seller_id=pk)
#         return Response(serializer.data, status.HTTP_201_CREATED)
# 
# 
# class PremiumSellerCarsUpdateRetrieveDestroyListView(RetrieveUpdateDestroyAPIView):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#     lookup_field = 'cars_id'  # перевірити чи працює


UserModel: User = get_user_model()


class PremiumSellerListView(ListAPIView):
    queryset = PremiumSellerModel.objects.all()
    serializer_class = PremiumSellerSerializer


class PremiumSellerView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.filter(roles='premium_seller')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)
        return (IsAuthenticated(),)


class PremiumSellerCarsListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.filter(roles='premium_seller')
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        exist = UserModel.objects.filter(pk=pk).exists()
        if not exist:
            raise Http404()
        cars = CarModelV2.objects.filter(premium_seller_id=pk)
        serializer = PremiumSellersCarsSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        serializer = PremiumSellersCarsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        exists = UserModel.objects.filter(pk=pk).exists()
        if not exists:
            raise Http404()
        serializer.save(premium_seller_id=pk)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    # def post(self, *args, **kwargs):
    #     pk = kwargs['pk']
    #     data = self.request.data
    #     serializer = PremiumSellersCarsSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     exists = UserModel.objects.filter(pk=pk).exists()
    #     if not exists:
    #         raise Http404()
    #     serializer.save(premium_seller_id=pk)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
