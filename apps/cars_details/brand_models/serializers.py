from rest_framework import serializers

from .models import CarBrandModel, CarsModelModel


class CarsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModelModel
        fields = ('id', 'brand', 'cars_model')

    # def validate(self, brand):
    #     if not brand:
    #         raise serializers.ValidationError('Brand is missing contact with manager manager@gmail.com')
    #     return brand


class CarBrandSerializer(serializers.ModelSerializer):
    cars_model = CarsModelSerializer(many=True, read_only=True)

    class Meta:
        model = CarBrandModel
        fields = ('id', 'brand', 'cars_model')

    def validate(self, brand):
        if not brand:
            raise serializers.ValidationError('Brand is missing contact with manager manager@gmail.com')
        return brand
