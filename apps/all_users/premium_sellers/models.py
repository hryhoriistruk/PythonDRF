from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

# from apps.all_users.accounts.models import AccountOfOwnersModel
# from apps.all_users.users.models import UserModel as User
#
# UserModel: User = get_user_model()
from apps.cars_details.cars.models import CarModelV2


class PremiumSellerModel(BaseModel):
    class Meta:
        db_table = 'premium_seller'
        ordering = ('id',)

    cars = models.ForeignKey(CarModelV2, on_delete=models.CASCADE, related_name="premium_sellers")
    # premium_seller = models.ForeignKey(AccountOfOwnersModel, on_delete=models.CASCADE, related_name="premium_sellers")
