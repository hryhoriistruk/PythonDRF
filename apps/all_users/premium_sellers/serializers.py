from datetime import datetime, timedelta

from django.db.models import Avg

from rest_framework import serializers

from apps.cars_details.cars.serializers import CarSerializer

from ...cars_details.cars.models import CarModelV2
from .models import PremiumSellerModel

# AdvertisementModel,

# ВИНЕСТИ ІНФОРМАЦІЮ В КАБІНЕТ КОРИСТОВАЧА
# class AdvertisementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdvertisementModel
#         fields = ('id', 'view_count')
#
#     def update_view_count(self, request, *args, **kwargs):
#         advertisement = AdvertisementModel.objects.all()
#         advertisement += 1
#         advertisement.save()
#         return advertisement
#
#
# def get_advertisement_last_day(self, request):
#     today = datetime.now().date()
#     yesterday = today - timedelta(days=1)
#     advertisements_views_last_day = AdvertisementModel.objects.filter(datedatetime_range=(today, yesterday))
#     num_advertisements_views_last_day = advertisements_views_last_day.count()
#     return num_advertisements_views_last_day
#
#
# def get_advertisement_last_week(self, request):
#     today = datetime.now().date()
#     last_week = today - timedelta(days=7)
#     advertisements_views_last_week = AdvertisementModel.objects.filter(datetime_range=(today, last_week))
#     num_advertisements_views_last_week = advertisements_views_last_week.count()
#     return num_advertisements_views_last_week
#
#
# def get_advertisement_last_month(self, request):
#     today = datetime.now().date()
#     last_month = today - timedelta(days=30)
#     advertisements_views_last_month = AdvertisementModel.objects.filter(datetime_range=(today, last_month))
#     num_advertisements_views_last_month = advertisements_views_last_month.count()
#     return num_advertisements_views_last_month


def average_price_in_region(price, region):
    average_price_by_regions = CarModel.objects.filter(region=region).aggregate(avg_price=Avg('price'))
    return average_price_by_regions['avg_price']


def average_price(price):
    average_price = CarModel.objects.aggregate(Avg('price'))
    return average_price['price__avg']


class PremiumSellerSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=False, read_only=True)

    class Meta:
        model = PremiumSellerModel
        fields = ('id', 'cars', 'premium_seller')

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     price = data['price']
    #     data['average_price_in_region'] = average_price_in_region(price, data['region'])
    #     data['average_price'] = average_price(price)
    #     advertisements_views = instance.car_views.count() #check
    #     # data['advertisements_views'] = advertisements_views #check
    #     # data['num_advertisements_views_last_day'] = get_advertisement_last_day(data['request'])
    #     # data['average_price'] = average_price(price)
    #     # data['update_view_count'] = data['update_view_count']
    #     return data


'''
ПОКАЗУВАТИ СЕРЕДНЮ ЦІНУ:
- ПО КРАЇНІ
- ПО РЕГІОНАМ
- К-ТЬ ПЕРЕГЛЯДІВ ОГОЛОШЕННЯ:
       * ЗА ДНЬ
       * ЗА ТИЖДЕНЬ
       * ЗА МІСЯЦЬ 
'''
