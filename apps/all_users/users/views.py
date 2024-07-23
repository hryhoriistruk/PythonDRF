from django.contrib.auth import get_user_model
from django.http import Http404

from rest_framework import status
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
    get_object_or_404,
)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.pagination import PagePagination
from core.permission import IsAdminOrWriteOnlyPermission
from core.services.email_service import EmailService

# from apps.all_users.users.models import UserAvatarModel
from apps.all_users.users.models import UserModel as User

# from ...cars_details.cars.models import CarModel
from ...cars_details.cars.serializers import CarSerializer
from ..accounts.models import AccountOfOwnersModel
from ..accounts.serializers import OwnerSerializer
from ..sellers.models import SellerModel
from .filters import UserFilter
from .serializers import ProfileSerializer, UserAvatarSerializer, UserSerializer

UserModel: User = get_user_model()


# class UserListCreateView(ListCreateAPIView):
#     serializer_class = UserSerializer
#     queryset = UserModel.objects.all()
# class RolesCreateAPIView(ListCreateAPIView):
#     serializer_class = RoleSerializer
#     queryset = RolesModel.objects.all()


# class UserListCreateView(ListCreateAPIView):
#     serializer_class = UserSerializer
#     queryset = UserModel.objects.all()

class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminOrWriteOnlyPermission,)

    # permission_classes = (AllowAny,)

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return (AllowAny(),)
    #     return (IsAdminUser(),)

    # pagination_class = PagePagination


# class UserAddAvatarView(GenericAPIView):
#     serializer_class = AvatarSerializer
class AddAvatarToProfileView(UpdateAPIView):
    serializer_class = UserAvatarSerializer
    http_method_names = ('put',)  # вказуємо який з методів будемо використовути, інший метод заблоковано

    def get_object(self):
        return UserModel.objects.all_with_profiles().get(pk=self.request.user.pk).profile

    def perform_update(self, serializer):
        self.get_object().avatar.delete()
        super().perform_update(serializer)


# class AddAvatarToProfileView(GenericAPIView):
#     serializer_class = UserAvatarSerializer
#     queryset = UserAvatarModel.objects.all()
#
#     def patch(self, *args, **kwargs):
#         profile = self.request.user.profile
#         files = self.request.FILES
#         for key in files:
#             serializer = self.serializer_class(data={'avatar': files[key]})
#             serializer.is_valid(raise_exception=True)
#             serializer.save(profile=profile)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def get(self, *args, **kwargs):
#         qs = self.queryset.filter(profile_id=self.request.user.profile.id)
#         serializer = UserAvatarSerializer(qs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class UpdateUserProfileView(GenericAPIView):
#     serializer_class = ProfileSerializer
#     queryset = UserModel.objects.all()
#
#     def patch(self, *args, **kwargs):
#         user = self.get_object()
#         data = self.request.data
#         serializer = self.serializer_class(user.profile, data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(user=user)
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class UsersListView(ListAPIView):
#     serializer_class = UserSerializer
#     queryset = UserModel.objects.all()
#     permission_classes = (IsAdminUser,)
#     filterset_class = UserFilter
#     pagination_class = PagePagination


class UserListRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)
    filterset_class = UserFilter
    pagination_class = PagePagination


# class MyView(GenericAPIView):
#     serializer_class = UserSerializer
#
#     def get_object(self):
#         return self.request.user
#
#     def get(self, *args, **kwargs):
#         serializer = UserSerializer(self.get_object())
#         return Response(serializer.data, status.HTTP_200_OK)

# .filter(is_superuser=False))
# filterset_class = UserFilters
# def get_queryset(self):
#     return User.objects.filter(roles='seller')

# def filter_queryset(self, queryset):
#     return super().filter_queryset(queryset).distinct()

# class SellerListCreateView(GenericAPIView):
#     serializer_class = SellerSerializer
#     queryset = SellerModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         user = self.request.user
#         serializer = UserSerializer(user)
#         return Response(serializer.data['sellers'], status=status.HTTP_200_OK)
#
#     # def post(self, *args, **kwargs):
#     #     user = self.request.user
#     #     data = self.request.data
#     #     serializer = self.serializer_class(data=data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save(user=user)
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def post(self, *args, **kwargs):
#         user = self.request.user
#         data = self.request.data
#         serializer = SellerSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         sellers: SellerModel = serializer.save()
#         sellers.users.add(user)
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     # def post(self, *args, **kwargs):
#     #     user = self.request.user
#     #     data = self.request.data
#     #     serializer = self.serializer_class(data=data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save(user=user)
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class SellerCarsListCreateView(GenericAPIView):
#     serializer_class = UserSerializer
#     queryset = UserModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
#         exist = UserModel.objects.filter(pk=pk).exists()
#         if not exist:
#             raise Http404()
#         cars = SellerModel.objects.filter(seller_id=pk)
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         exists = UserModel.objects.filter(pk=pk).exists()
#         if not exists:
#             raise Http404()
#         serializer.save(seller_id=pk)
#         return Response(serializer.data, status.HTTP_201_CREATED)

class TestEmailView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        EmailService.test_email()
        return Response('ok')


class OwnerAccountListView(ListCreateAPIView):
    serializer_class = OwnerSerializer
    queryset = AccountOfOwnersModel.objects.all()

    # def post(self, *args, **kwargs):
    #     pk = kwargs['pk']
    #     owner = get_object_or_404(UserModel, pk=pk, roles='owner')
    #     owner.base_account = 'base_account'
    #     serializer = OwnerSerializer(owner)
    #     serializer.is_valid(raise_exception=True)
    #     owner.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
