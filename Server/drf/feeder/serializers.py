from rest_framework import serializers
from .models import FeederStatus

class FeederStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeederStatus
        fields = '__all__'  