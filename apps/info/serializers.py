from rest_framework import serializers

from .models import Info


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        db_table = 'info'
        fields = '__all__'