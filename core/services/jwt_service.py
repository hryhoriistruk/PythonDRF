from typing import Type

from rest_framework_simplejwt.tokens import Token, BlacklistMixin
from core.enums.action_token_enum import ActionTokenEnum
from rest_framework.generics import get_object_or_404

ActionTokenClassType = Type[BlacklistMixin | Token]
from django.contrib.auth import get_user_model
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class ActionToken(BlacklistMixin, Token):
    pass


class ActivateToken(ActionToken):
    token_type = ActionTokenEnum.ACTIVATE.token_type
    lifetime = ActionTokenEnum.ACTIVATE.life_time


class RecoveryToken(ActionToken):
    token_type = ActionTokenEnum.RECOVERY.token_type
    lifetime = ActionTokenEnum.RECOVERY.life_time


class JWTService:
    @staticmethod
    def create_token(user, token_class: ActionTokenClassType):
        return token_class.for_user(user)

    @staticmethod
    def validate_token(token, token_class: ActionTokenClassType):
        try:
            token_res = token_class(token)
            token_res.check_blacklist()
        except Exception as err:
            print(err)

        token_res.blacklist()
        user_id = token_res.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)
