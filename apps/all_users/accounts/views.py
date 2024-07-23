from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.all_users.accounts.serializers import OwnerSerializer
from apps.all_users.users.models import UserModel as User

UserModel: User = get_user_model()


# class OwnerAccountListView(APIView):
#     serializer_class = OwnerSerializer
#
#
#     def post(self, *args, **kwargs):
#         pk = kwargs['pk']
#         owner = get_object_or_404(UserModel, pk=pk, roles='owner')
#         owner.base_account='base_account'
#         serializer = OwnerSerializer(owner)
#         serializer.is_valid(raise_exception=True)
#         owner.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)



# class ChangeAccountToPremiumView(APIView):
#     serializer_class = OwnerSerializer
#
#     def patch(self, *args, **kwargs):
#         # seller = kwargs['pk']
#         # user = UserModel.objects.get(pk=seller)
#         # user.roles = 'premium_seller'
#         # # # user.roles.premium_seller = True
#         # serializer = UserSerializer(user)
#         # # print(user)
#         # user.save()
#         # # return Response(serializer.data, status=status.HTTP_200_OK)
#         # # else Response({'message':'error':'You are not authorized to perform this action'}, status=status.403_FORBIDDEN)
#         owner = get_object_or_404(UserModel, id=kwargs['pk'], roles='owner')
#         owner.premium_account = 'premium_account'
#         serializer = OwnerSerializer(owner)
#         owner.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
