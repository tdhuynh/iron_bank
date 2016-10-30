from rest_framework import serializers

from iron_bank_api.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='account.id')
    class Meta:
        model = Transaction
        exclude = ('account',)
