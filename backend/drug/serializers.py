from rest_framework import serializers
from .models import Drug

class UserSerializers(serializers.Serializer):
    class Meta:
        model: Drug
        fields: '__all__'