from rest_framework import serializers
from .models import Store

class StoreSerializers(serializers.Serializer):
    class Meta:
        model: Store
        fields: '__all__'