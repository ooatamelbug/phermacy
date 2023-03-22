from rest_framework import serializers
from .models import Stock, StoreStock

class StockSerializers(serializers.Serializer):
    class Meta:
        model: Stock
        fields: '__all__'


class StoreStockSerializers(serializers.Serializer):
    class Meta:
        model: StoreStock
        fields: '__all__'