from django.db import models

from core.models import BaseModel


class AdminCarDealershipModel(BaseModel):
    class Meta:
        db_table = 'car_dealership_admin'

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
