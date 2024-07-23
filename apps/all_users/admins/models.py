# from django.contrib.auth import get_user_model
# from django.db import models
#
# from core.models import BaseModel
#
# from apps.all_users.users.models import UserModel as User
#
# UserModel: User = get_user_model()
# from apps.all_users.users.models import ProfileModel

# class AdminModel(BaseModel):
#     class Meta:
#         db_table = 'admins'
#         ordering = ('id',)
#
#     profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='profile')
#     users = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auth_user')
