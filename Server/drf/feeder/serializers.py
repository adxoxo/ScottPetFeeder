from rest_framework import serializers
from .models import FeederStatus

class FeederStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeederStatus
        fields = '__all__'

class FoodLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeederStatus
        fields = ['food_level_low']

class ManualModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeederStatus
        fields = ['is_manual_mode']