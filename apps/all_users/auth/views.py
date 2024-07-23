from django.contrib.auth import get_user_model
from django.http import Http404

from rest_framework import status
from rest_framework.generics import (
    GenericAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

from apps.all_users.auth.serializers import EmailSerializer, PasswordSerializer
from apps.all_users.users.models import ProfileModel
from apps.all_users.users.models import UserModel as User

UserModel: User = get_user_model()
from apps.all_users.users.serializers import ProfileSerializer, UserSerializer

# class MeView(GenericAPIView):
#     def get(self, *args, **kwargs):
#         user = self.request.user
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class MeView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        token = kwargs['token']
        user:UserModel = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecoveryPasswordRequest(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, **serializer.data)
        EmailService.recovery_password(user)
        return Response('Check your email to reset your password', status=status.HTTP_200_OK)

class RecoveryPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class =PasswordSerializer

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        user:User = JWTService.validate_token(token, RecoveryToken)
        user.set_password(serializer.data['password'])
        user.save()
        return Response('Password changed', status=status.HTTP_200_OK)


class UpdateUserProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializer = self.serializer_class(user.profile, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class RecoverySendEmailView(GenericAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = UserSerializer
#
#     def post(self, *args, **kwargs):
#         email = kwargs.get('email')
#         user = get_object_or_404(UserModel, email=email)
#         EmailService.recovery_password(user)
#         return Response(status=status.HTTP_200_OK)
#
#
# class RecoverySetPasswordView(GenericAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = PasswordSerializer
#
#     def post(self, *args, **kwargs):
#         token = kwargs.get('token')
#         new_password = kwargs.get('password')
#         serializer = PasswordSerializer(data={'password': new_password})
#         serializer.is_valid(raise_exception=True)
#         user = JWTService.validate_token(token, RecoveryToken)
#         user.set_password(new_password)
#         user.save()
#         return Response({'details': 'password saved'}, status=status.HTTP_200_OK)


# написати код на зміну пароля, попробувати винести інформацію  по машинах для преміум продавців
# винести код для зміни даних по товару продавця
