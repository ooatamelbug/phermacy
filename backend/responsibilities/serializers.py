from rest_framework import serializers
from .models import Responsibilities, UserResponsibilities

class ResponsibilitiesSerializers(serializers.Serializer):
    class Meta:
        model: Responsibilities
        fields: '__all__'



class UserResponsibilitiesSerializers(serializers.Serializer):
    class Meta:
        model: UserResponsibilities
        fields: '__all__'
