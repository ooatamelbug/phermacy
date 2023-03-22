from rest_framework import serializers
from .models import StockTransfer

class StockTransferSerializers(serializers.Serializer):
    class Meta:
        model: StockTransfer
        fields: '__all__'

