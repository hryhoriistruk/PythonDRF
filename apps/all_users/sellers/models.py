from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from core.models import BaseModel

# from apps.all_users.users.models import UserModel as User
from apps.cars_details.cars.models import CarModelV2

# UserModel: User = get_user_model()


class SellerModel(BaseModel):
    class Meta:
        db_table = 'seller'
        ordering = ('id',)

    #
    #     name = models.CharField(max_length=25)
    #     surname = models.CharField(max_length=25)
    #     email = models.EmailField(unique=True)
    #     password = models.CharField(max_length=128)
    #     phone_number = models.IntegerField(unique=True, null=True, blank=True)
    #     company_name = models.CharField(max_length=25, null=True, blank=True)
    #     position = models.CharField(max_length=20, null=True, blank=True)
    cars = models.ForeignKey(CarModelV2, on_delete=models.CASCADE, related_name='cars')
    # seller = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auth_user')


#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='sellers')
#
#
# # class UserSellerModel(models.Model):
# #     class Meta:
# #         db_table = 'users_sellers'
# #
# #     user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
# #     seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE

# class UserProfileModel(BaseModel):
#     class Meta:
#         db_table = 'seller_car'
#
#         seller = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auth_user')
#         car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='cars')
