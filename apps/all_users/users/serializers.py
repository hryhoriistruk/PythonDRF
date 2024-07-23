from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers

from core.services.email_service import EmailService

# from apps.all_users.users.models import RolesModel
# from apps.all_users.users.models import UserAvatarModel
from apps.all_users.users.models import UserModel as User

from ...cars_details.cars.serializers import CarSerializer
from ..accounts.models import AccountOfOwnersModel
# from ..sellers.serializers import SellerSerializer
from .models import ProfileModel

UserModel: User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'user', 'avatar',)
        read_only_fields = ('user', 'avatar',)


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        # model = UserAvatarModel
        model = ProfileModel
        fields = ('avatar',)
        # read_only_fields = ('profile',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_superuser', 'is_staff', 'created_at', 'updated_at',
            'last_login', 'profile', 'roles', 'cars',
        )
        read_only_fields = (
            'id', 'created_at', 'updated_at', 'is_superuser', 'last_login', 'is_active', 'cars',)
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        # if validated_data.get('roles') == 'owner':
        #     AccountOfOwnersModel.objects.create(base_account=user)
        EmailService.register_email(user)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()

        if profile_data:
            profile = instance.profile
            profile.name = profile_data.get('name', profile.name)
            profile.surname = profile_data.get('surname', profile.surname)
            profile.phone_number = profile_data.get('phone_number', profile.phone_number)
            profile.save()
        return instance
