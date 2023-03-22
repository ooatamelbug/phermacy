from rest_framework import serializers
from .models import StockRequest

class StockRequestSerializers(serializers.Serializer):
    class Meta:
        model: StockRequest
        fields: '__all__'

