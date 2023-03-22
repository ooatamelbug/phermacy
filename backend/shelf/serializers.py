from rest_framework import serializers
from .models import Shelf, ShelfDrug

class ShelfSerializers(serializers.Serializer):
    class Meta:
        model: Shelf
        fields: '__all__'




class ShelfDrugSerializers(serializers.Serializer):
    class Meta:
        model: ShelfDrug
        fields: '__all__'