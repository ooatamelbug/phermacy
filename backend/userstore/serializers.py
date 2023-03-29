from rest_framework import serializers
from .models import UserStore

class UserStoreSerializers(serializers.Serializer):
    class Meta:
        model= UserStore
        fields= '__all__'

