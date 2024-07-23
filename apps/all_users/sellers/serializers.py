# from django.contrib.auth import get_user_model
# from django.db import transaction
#
from django.http import Http404
from django.shortcuts import redirect

from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.all_users.sellers.models import SellerModel
from apps.cars_details.cars.serializers import CarSerializer

#
# from apps.all_users.sellers.models import SellerModel
#
# from ..users.models import UserModel as User
# from ..users.serializers import UserSerializer
#
# UserModel: User = get_user_model()
#
#
# class SellerModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SellerModel
#         fields = ('id', 'name', 'surname', 'password', 'phone_number', 'user', 'company_name', 'position')
#         read_only_fields = ('user',)
#
#
# @api_view['POST']
# def add_cars(request):
#     seller_id = request.data.get['seller_id']
#     if seller_can_add_more_cars(seller_id):
#
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         exists = UserModel.filter(pk=pk).exists()
#         if not exists:
#             raise Http404()
#         serializer.save(seller_id=pk)
#         # return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'message': 'You add car'}, status=status.HTTP_201_CREATED)
#     else:
#         payment_url = 'your payment url here'
#         return redirect(payment_url)


class SellerSerializer(serializers.ModelSerializer):
    car = CarSerializer(many=False, read_only=True)

    class Meta:
        model = SellerModel
        fields = ('id', 'car', 'sellers')
#
