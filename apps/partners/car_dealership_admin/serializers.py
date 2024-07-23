from rest_framework import serializers

from .models import AdminCarDealershipModel


class AdminCarDealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminCarDealershipModel
        fields = ('id', 'name', 'surname', 'email', 'phone_number')
