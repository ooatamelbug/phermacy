from rest_framework import serializers
from .models import PurchaseOrder

class PurchaseOrderSerializers(serializers.Serializer):
    class Meta:
        model: PurchaseOrder
        fields: '__all__'

