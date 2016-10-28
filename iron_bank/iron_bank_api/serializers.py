from rest_framework import serializers

from iron_bank_api.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    
