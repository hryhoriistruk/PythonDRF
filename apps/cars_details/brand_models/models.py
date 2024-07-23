from django.core import validators
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db import models

from core.enums.regex_enums import RegexEnum
from core.models import BaseModel


# def validate_brand(self, brand):
#     if not brand:
#         send_mail(
#             'Brand not available',
#             'The serializer did not receive any data',
#             'from@example.com',  # виправити на email продавця
#             ['manager@example.com'],
#             fail_silently=False,
#         )
#     return brand
class CarBrandModel(BaseModel):
    class Meta:
        db_table = 'car_brand'
        ordering = ('id',)

    brand = models.CharField(max_length=25, unique=True, validators=[
        validators.RegexValidator(RegexEnum.BRAND.pattern, RegexEnum.BRAND.msg),
    ])

    # def save(self, *args, **kwargs):
    #     if not self.brand:
    #         raise ValidationError('Brand is missing contact with manager manager@gmail.com')
    #     super(CarBrandModel, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if self.brand is None:
    #         raise ValidationError('Brand is missing contact with manager manager@gmail.com')
    #     super(CarBrandModel, self).save(*args, **kwargs)

    # def validate_brand(self, data):
    #     if not data['brand']:
    #         raise ValidationError('Brand is missing contact with manager manager@gmail.com')
    #     return data

    # def __str__(self):
    #     return self.brand


class CarsModelModel(BaseModel):
    class Meta:
        db_table = 'cars_model'
        ordering = ('id',)

    cars_model = models.CharField(max_length=25)
    brand = models.ForeignKey(CarBrandModel, on_delete=models.CASCADE, related_name='cars_model')

    def __str__(self):
        return self.cars_model
