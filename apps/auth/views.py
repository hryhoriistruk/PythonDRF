from rest_framework.generics import GenericAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from apps.users.serializers import UserSerializer
from core.dataclasses.user_dataclass import UserDataClass
from core.services.email_service import EmailService
from core.services.jwt_service import JWTService, ActivateToken, RecoveryToken
from apps.users.models import UserModel as User
from .serializers import EmailSerializer, PasswordSerializer
from django.contrib.auth import get_user_model
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class MeView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        token = kwargs['token']
        user: User = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class RecoveryPasswordRequestView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, **serializer.data)
        EmailService.recovery_password(user)
        return Response('Check your email', status.HTTP_200_OK)


class RecoveryPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordSerializer

    def post(self, *args, **kwargs):
        data = self.request.data # дістали password
        serializer = self.get_serializer(data=data) #отримали екземпляр serializer
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        user:User = JWTService.validate_token(token, RecoveryToken)
        user.set_password(serializer.data['password'])
        user.save()
        return Response('password changed', status.HTTP_200_OK)



