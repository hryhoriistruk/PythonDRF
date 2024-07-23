from rest_framework import serializers

from apps.all_users.accounts.models import AccountOfOwnersModel


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountOfOwnersModel
        fields = ('id', 'owner', 'created_at', 'updated_at', 'base_account', 'premium_account',)
        read_only_fields = ('owner', 'created_at', 'updated_at', 'base_account', 'premium_account')


    # def create(self, validated_data):
    #     return AccountOfOwnersModel.objects.create(**validated_data)
