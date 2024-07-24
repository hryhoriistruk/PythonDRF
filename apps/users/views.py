from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, GenericAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.users.models import UserModel as User
from core.permissions import IsAdminOrWriteOnlyPermission, IsSuperUser

from .filters import UserFilter
from rest_framework.permissions import AllowAny, IsAdminUser

UserModel: User = get_user_model()
from .serializers import UserSerializer, AvatarSerializer
from core.services.email_service import EmailService


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    filterset_class = UserFilter
    # permission_classes = (AllowAny,)
    permission_classes = (IsAdminOrWriteOnlyPermission,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return (IsAdminUser(),)
        return super().get_permissions()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)


# class UserAddAvatarView(GenericAPIView):
#     serializer_class = AvatarSerializer
#
#     def put(self, *args, **kwargs):
#         # serializer = AvatarSerializer(self.request.user.profile, data=self.request.FILES,
#         #                               context={'request': self.request})
#         serializer = self.get_serializer(self.request.user.profile, data=self.request.FILES)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)

class UserAddAvatarView(UpdateAPIView):  # підкапотно використовує два методи put and patch
    serializer_class = AvatarSerializer
    http_method_names = ('put',)  # вказуємо який з методів будемо використовути, інший метод заблоковано

    def get_object(self):
        return UserModel.objects.all_with_profiles().get(pk=self.request.user.pk).profile

    def perform_update(self, serializer):
        self.get_object().avatar.delete()
        super().perform_update(serializer)


class UserToAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user: User = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class BlockUserView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UnBlockUserView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class BlockAdminUserView(BlockUserView):
    permission_classes = (IsSuperUser,)


class UnBlockAdminUserView(UnBlockUserView):
    permission_classes = (IsSuperUser,)


class TestEmailView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        EmailService.test_email()
        return Response('ok')
