from datetime import date, datetime, timedelta

from django.contrib.auth import get_user_model

from apps.all_users.users.models import UserModel as User

UserModel: User = get_user_model()
from django.contrib import messages
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models, transaction
from django.db.models import Avg, Count, manager
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

import requests

from core.enums.regex_enums import RegexEnum
from core.services.email_service import EmailService

from .models import CarModelV2, CarPhotosModel

# class ProductPhotoSerializer(ModelSerializer):
#     class Meta:
#         model = ProductPhotosModel
#         fields = ('id', 'photo')

# def to_representation(self, instance: ProductPhotosModel):
#     return {
#         "id": instance.id,
#         "photo": instance.photo.url
#     }


# class ProductSerializer(ModelSerializer):
#     photos = ProductPhotoSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = ProductModel
#         fields = (
#             'id', 'created_at', 'category', 'producer', 'material', 'length', 'clasp', 'price', 'discounts', 'amount', 'solded',
#             'photos')
class CarPhotosListSerializer(serializers.Serializer):
    image = serializers.ListField(child=serializers.ImageField())

    class Meta:
        model = CarPhotosModel
        fields = ('id', 'image',)

    def to_representation(self, instance: CarPhotosModel):
        return {
            "id": instance.id,
            "image": instance.image.url
        }

    # def create(self, validated_data):
    #     print("self.context", self.context)
    #     car = self.context['car']
    #     print('car', car)
    #
    #     # user = validated_data['seller']
    #     # photos = validated_data.pop('photos')
    #     # car = CarModel.objects.create(**validated_data)
    #     for image in validated_data['images']:
    #         CarPhotosModel.objects.create(car=car, image=image)
    #     # # EmailService.created_car_by_seller(user, car)
    #     return car


def average_price_in_region(price, region):
    average_price_by_regions = CarModelV2.objects.filter(region=region).aggregate(avg_price=Avg('price'))
    return average_price_by_regions['avg_price']


def average_price(price):
    average_price = CarModelV2.objects.aggregate(Avg('price'))
    return average_price['price__avg']


# def average_price_for_same_car_by_parameters(price, brand, cars_model):
#     # global average_price_for_same_car_by_parameters
#     filtered_cars = CarModel.objects.filter(brand=brand, cars_model=cars_model)
#     if filtered_cars.exists():
#         total_price = sum(car.price for car in filtered_cars)
#         average_price_for_same_car_by_parameters = total_price / len(filtered_cars)
#     return average_price_for_same_car_by_parameters['average_price_for_same_car_by_parameters']


def get_currency_exchange_rates():
    response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
    data = response.json()
    exchange_rates = {}
    for currency in data:
        if currency['ccy'] in ['USD', 'EUR']:
            exchange_rates[currency['ccy']] = float(currency['buy'])
    return exchange_rates


def calculate_price_in_currency(price, currencies):
    exchange_rates = get_currency_exchange_rates()
    recalculated_prices = {}
    for currency in currencies:
        recalculated_prices[currency] = price / exchange_rates[currency]
    return recalculated_prices


#################################################################################################
def validate_description(description):
    obscene_words = [
        "FUCK",
        "asshole",
        "fucking",
        "fuck"
    ]
    for word in obscene_words:
        if word in description.lower():
            raise ValidationError({'error': 'Obscene word found in description'})
    return description


class CarSerializer(serializers.ModelSerializer):
    image = CarPhotosListSerializer(read_only=True, many=True)

    class Meta:
        model = CarModelV2
        fields = (
            'id', 'brand', 'cars_model', 'price', 'seller', 'currency', 'premium_seller', 'description',
            'blocked', 'attempts',
            'image',
            # 'uploaded_photos',
            # 'color', 'year', 'seat_count', 'body_type',
            # 'engine_type',
            # 'engine_volume',
            # 'transmission', 'mileage',
            'region',
        )
        read_only_fields = ('seller', 'premium_seller', 'attempts', 'blocked', 'image'
                            # 'photos',
                            # 'uploaded_photos'
                            )

    def validate(self, data):
        description = data.get('description')
        attempts = data.get('attempts', 0)
        blocked = data.get('blocked')
        if validate_description(description):
            attempts += 1
            if attempts == 3:
                blocked = True
                return ValidationError({'error': 'You car is blocked'})
        return data

    # def create(self, validated_data):
    #     # user = validated_data['seller_id']
    #     # print(validated_data)
    #     # photos = validated_data.pop('photos')
    #     car = CarModel.objects.create(**validated_data)
    #     # for photo in photos:
    #     #     CarPhotosModel.objects.create(car=car, photo=photo)
    #     # EmailService.created_car_by_seller(user, car)
    #     return car

    def to_representation(self, instance):
        data = super().to_representation(instance)
        price = data['price']
        recalculated_prices = calculate_price_in_currency(price, ['USD', 'EUR'])
        data['price_usd'] = recalculated_prices['USD']
        data['price_eur'] = recalculated_prices['EUR']
        return data


##########################################################################
class PremiumSellersCarsSerializer(CarSerializer):
    class Meta:
        model = CarModelV2
        fields = (
            'id', 'brand', 'cars_model', 'price', 'seller', 'currency', 'premium_seller', 'region',
            'description',
            'blocked', 'attempts',

        )
        read_only_fields = ('seller', 'premium_seller', 'attempts', 'blocked', 'photos'
                            )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        price = data['price']
        data['average_price_in_region'] = average_price_in_region(price, data['region'])
        # data['average_price_for_same_car_by_parameters'] = average_price_for_same_car_by_parameters(price, data[
        #     'brand', 'cars_model'])
        data['average_price'] = average_price(data['price'])
        return data
