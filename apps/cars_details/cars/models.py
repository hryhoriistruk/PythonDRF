import re
from datetime import datetime

from django.contrib.auth import get_user_model
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# UserModel: User = get_user_model()
from core.enums.regex_enums import RegexEnum
from core.models import BaseModel
from core.services.upload_photos_to_car_service import upload_photos_to_car

from ..brand_models.models import CarBrandModel, CarsModelModel
from .choices import *
from .managers import CarManager

#
# from apps.all_users.users.models import ProfileModel
# from apps.all_users.users.models import UserModel as User

# from .managers import check_description



# class CarModel(BaseModel):
#     class Meta:
#         db_table = 'cars'
#         ordering = ('id',)
#
#     brand = models.ForeignKey(CarBrandModel, on_delete=models.CASCADE, related_name='cars')
#     cars_model = models.ForeignKey(CarsModelModel, on_delete=models.CASCADE, related_name='cars')
#     # model = models.CharField(max_length=25, validators=(
#     #     validators.RegexValidator(RegexEnum.MODEL.pattern, RegexEnum.MODEL.msg),
#     # )
#     #                          )
#     # color = models.CharField(max_length=25
#     #                          #                          , validators=(
#     #                          #     validators.RegexValidator(RegexEnum.COLOR.pattern, RegexEnum.COLOR.msg)
#     #                          # )
#     #                          )
#     # year = models.IntegerField(validators=(
#     #     validators.MinValueValidator(1885),
#     #     validators.MaxValueValidator(datetime.now().year)
#     # )
#     # )
#     price = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000000)])
#     currency = models.CharField(max_length=3, choices=CurrencyChoices.choices, default='UAH')
#     # seat_count = models.IntegerField(default=0)
#     # body_type = models.CharField(max_length=11, choices=BodyTypeChoices.choices)
#     # engine_type = models.CharField(max_length=25, choices=EngineTypesChoices.choices)
#     # engine_volume = models.FloatField(default=0)
#     # transmission = models.CharField(max_length=25, choices=TransmissionTypeChoices.choices)
#     # mileage = models.IntegerField()
#     region = models.CharField(max_length=25)
#     premium_seller = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='premium_seller', null=True)
#     seller = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='seller', null=True)
#     # image = models.ImageField()
#     # description = models.TextField(max_length=255, validators=[ObsceneLanguageValidator])
#     # description = models.TextField(max_length=255, validators=[check_description])
#     description = models.TextField(max_length=255)
#     # description = models.TextField(max_length=255, validators=[validate_description])
#     # description = models.TextField(max_length=255, validators=(
#     #     validators.RegexValidator(RegexEnum.DESCRIPTION.pattern, RegexEnum.DESCRIPTION.msg),
#     # ))
#     attempts = models.IntegerField(default=0)
#     blocked = models.BooleanField(default=False)
#
#     objects = CarManager()

# class AccountOfOwnersModel(BaseModel):
#     class Meta:
#         db_table = 'accounts_of_owners'
#         ordering = ('id',)
#
#     base_account = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='base_account')
#     premium_account = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='premium_account')


class CarModelV2(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    brand = models.ForeignKey(CarBrandModel, on_delete=models.CASCADE, related_name='cars')
    cars_model = models.ForeignKey(CarsModelModel, on_delete=models.CASCADE, related_name='cars')
    # model = models.CharField(max_length=25, validators=(
    #     validators.RegexValidator(RegexEnum.MODEL.pattern, RegexEnum.MODEL.msg),
    # )
    #                          )
    # color = models.CharField(max_length=25
    #                          #                          , validators=(
    #                          #     validators.RegexValidator(RegexEnum.COLOR.pattern, RegexEnum.COLOR.msg)
    #                          # )
    #                          )
    # year = models.IntegerField(validators=(
    #     validators.MinValueValidator(1885),
    #     validators.MaxValueValidator(datetime.now().year)
    # )
    # )
    price = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000000)])
    currency = models.CharField(max_length=3, choices=CurrencyChoices.choices, default='UAH')
    # seat_count = models.IntegerField(default=0)
    # body_type = models.CharField(max_length=11, choices=BodyTypeChoices.choices)
    # engine_type = models.CharField(max_length=25, choices=EngineTypesChoices.choices)
    # engine_volume = models.FloatField(default=0)
    # transmission = models.CharField(max_length=25, choices=TransmissionTypeChoices.choices)
    # mileage = models.IntegerField()
    region = models.CharField(max_length=25)
    # premium_seller = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='premium_seller',
    #                                    null=True)
    # seller = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='seller', null=True)
    # image = models.ImageField()
    # description = models.TextField(max_length=255, validators=[ObsceneLanguageValidator])
    # description = models.TextField(max_length=255, validators=[check_description])
    description = models.TextField(max_length=255)
    # description = models.TextField(max_length=255, validators=[validate_description])
    # description = models.TextField(max_length=255, validators=(
    #     validators.RegexValidator(RegexEnum.DESCRIPTION.pattern, RegexEnum.DESCRIPTION.msg),
    # ))
    # attempts = models.IntegerField(default=0)
    # blocked = models.BooleanField(default=False)
    # owner = models.ForeignKey(AccountOfOwnersModel, on_delete=models.CASCADE, related_name='cars')
    objects = CarManager()


class CarPhotosModel(BaseModel):
    class Meta:
        db_table = 'car_photos'
        ordering = ('id',)

    image = models.ImageField(upload_to=upload_photos_to_car, null=True, blank=True)
    car = models.ForeignKey(CarModelV2, on_delete=models.CASCADE, related_name='avatars')
