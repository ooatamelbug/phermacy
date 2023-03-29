from rest_framework import serializers
from .models import Supplier

class SupplierSerializers(serializers.Serializer):
    class Meta:
        model= Supplier
        fields= '__all__'
