from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

from apps.all_users.users.models import ProfileModel
from apps.all_users.users.models import UserModel as User

UserModel: User = get_user_model()
from core.models import BaseModel


class ManagerModel(BaseModel):
    class Meta:
        db_table = 'manager'
        ordering = ('id',)

    # profile=models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='profile')
    # user=models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auth_user')
    