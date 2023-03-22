from rest_framework import serializers
from .models import PurchaseDrug

class PurchaseDrugSerializers(serializers.Serializer):
    class Meta:
        model: PurchaseDrug
        fields: '__all__'

