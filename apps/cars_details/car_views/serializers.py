from datetime import timedelta

from django.utils import timezone

from rest_framework import serializers

from apps.cars_details.car_views.models import CarViewModel


def views_per_day(views):
    start_time = timezone.now() - timedelta(days=1)
    end_time = timezone.now()
    views_count_per_day = (CarViewModel.objects.filter(created_at__gte=start_time, updated_at__lte=end_time).count())
    return views_count_per_day


def views_per_week(views):
    start_time = timezone.now() - timedelta(days=7)
    end_time = timezone.now()
    views_count_per_week = (CarViewModel.objects.filter(created_at__gte=start_time, updated_at__lte=end_time).count())
    return views_count_per_week


def views_per_month(views):
    start_time = timezone.now() - timedelta(days=30)
    end_time = timezone.now()
    views_count_per_month = (CarViewModel.objects.filter(created_at__gte=start_time, updated_at__lte=end_time).count())
    return views_count_per_month


class CarViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarViewModel
        fields = ('id', 'car_ad', 'views',)
        read_only_fields = ('car_ad', 'views',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        views = data['views']
        data['views_count_per_day'] = views_per_day(views)
        data['views_count_per_week'] = views_per_week(views)
        data['views_count_per_month'] = views_per_month(views)
        return data
