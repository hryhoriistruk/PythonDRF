from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers

from apps.users.models import ProfileModel, AvatarModel
from apps.users.models import UserModel as User
from core.services.email_service import EmailService

UserModel: User = get_user_model()


class UserAvatarListSerializer(serializers.Serializer):
    images = serializers.ListField(child=serializers.ImageField())

    def to_representation(self, instance):
        return UserSerializer(self.context['profile'].user, context={'request': self.context['request']}).data

    def create(self, validated_data):
        profile = self.context['profile']
        print(validated_data)
        for image in validated_data['images']:
            AvatarModel.objects.create(image=image, profile=profile)
        return profile.user

    # def to_representation(self, instance):
    #     return UserSerializer(self.context['profile'].user).data
    #
    # def create(self, validated_data):
    #     profile = self.context['profile']
    #     for image in validated_data['images']:
    #         AvatarModel.objects.create(image=image, profile=profile)
    #     return profile.user


#                                           FOR UPLOAD ONE PHOTO
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProfileModel
#         fields = ('id', 'name', 'surname', 'age', 'avatar',)

#                                          FOR UPLOAD MANY PHOTOS
class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        # model = ProfileModel
        model = AvatarModel
        # fields = ('avatar',)
        fields = ('image',)
        extra_kwargs = {
            'avatar': {
                'required': True
            }
        }


class ProfileSerializer(serializers.ModelSerializer):
    avatars = AvatarSerializer(read_only=True, many=True)

    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'avatars',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at',
            'profile'
        )
        read_only_fields = ('is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at',)
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate_email(self, email: str):
        if not email.endswith('@gmail.com'):
            raise serializers.ValidationError('email must be gmail.com host')
        return email

    @transaction.atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        profile = ProfileModel.objects.create(**profile)
        user = UserModel.objects.create_user(profile=profile, **validated_data)
        EmailService.register_email(user)
        return user
