from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.models import BaseModel
from core.services import upload_avatar

# from ..accounts.models import AccountOfOwnersModel
from .managers import UserManager
from .roles_choices import RolesChoices

# class AccountOfOwnersModel(BaseModel):
#     class Meta:
#         db_table = 'accounts_of_owners'
#         ordering = ('id',)
#
#     base_account = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='base_account')
#     premium_account = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='premium_account')


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'
        ordering = ('id',)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    roles = models.CharField(max_length=17, choices=RolesChoices.choices)
    # cars = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='cars')
    # accounts_of_owners = models.OneToOneField(AccountOfOwnersModel, on_delete=models.CASCADE, related_name='accounts', null=True, blank=True)
    USERNAME_FIELD = 'email'

    objects = UserManager()

    # def filter_by_roles(self, roles):
    #     return self.filter(roles=roles)


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    phone_number = models.IntegerField(unique=True, null=True, blank=True)
    company_name = models.CharField(max_length=25, null=True, blank=True)
    position = models.CharField(max_length=20, null=True, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    # avatar = models.ImageField(upload_to='image', blank=True)
    # role = models.OneToOneField(RolesModel, on_delete=models.CASCADE, related_name='+')
    # roles = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='auth_user')
    avatar = models.ImageField(upload_to=upload_avatar, blank=True)

# class UserAvatarModel(models.Model):
#     class Meta:
#         db_table = 'user_avatar'
#
#     avatar = models.ImageField(upload_to=upload_avatar, blank=True)
#     profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='avatar')

# class ProfileModel(models.Model):
#     class Meta:
#         db_table = 'profile'
# age = models.IntegerField(validators=[
#     val.MinValueValidator(1), val.MaxValueValidator(100)
# ])
# house = models.CharField(max_length=30)
# phone = models.CharField(max_length=15, validators=[
#     val.RegexValidator(RegEx.PHONE.pattern, RegEx.PHONE.message)
# ])
# avatar = models.ImageField(upload_to=upload_avatar, blank=True)
# user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
