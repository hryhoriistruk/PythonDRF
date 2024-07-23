from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.all_users.users.models import UserModel as User

UserModel: User = get_user_model()
from core.permission.is_super_user import IsSuperUser

from apps.all_users.users.serializers import UserSerializer


class UserToManagerView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user: User = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.roles = 'manager'
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class ManagerToUserView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user:User = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.roles = 'visitor'
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class BanManagerView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user:User = self.get_object()
        if user.is_active:
            user.is_active = False
            user.roles = 'blocked'
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UnBanManagerView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user:User = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.roles = 'manager'
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
