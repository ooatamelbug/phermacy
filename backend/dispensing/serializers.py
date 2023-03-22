from rest_framework import serializers
from .models import Dispensing, SoldDrug

class DispensingSerializers(serializers.Serializer):
    class Meta:
        model: Dispensing
        fields: '__all__'



class SoldDrugSerializers(serializers.Serializer):
    class Meta:
        model: SoldDrug
        fields: '__all__'