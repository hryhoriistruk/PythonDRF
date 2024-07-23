from rest_framework import serializers

from .models import VisitorModel


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorModel
        fields = ('id', 'name', 'surname', 'email', 'password', 'phone_number')