from rest_framework import serializers
from .models import CarDealershipModel


class CarDealerShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDealershipModel
        fields = ('id', 'name')
