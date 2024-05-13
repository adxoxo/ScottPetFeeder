from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework import status 
from rest_framework.response import Response
from .models import FeederStatus
from .serializers import FeederStatusSerializer, FoodLevelSerializer, ManualModeSerializer

# Create your views here.

class PetFeederView(ViewSet):

    def manual_mode_view(self, request):

        manual_status, created = FeederStatus.objects.get_or_create()
        is_on = manual_status.is_manual_mode
        serializer = ManualModeSerializer({
            'is_manual_mode':is_on
        })
        manual_mode = serializer.data['is_manual_mode']
        return Response ({
            manual_mode
        })


    def food_level_view(self, request):

        serializer = FoodLevelSerializer(data=request.data)
        if serializer.is_valid():
            # Retrieve or create the FeederStatus instance
            feeder_status, created = FeederStatus.objects.get_or_create()

            # Update the food_level_low field
            feeder_status.food_level_low = serializer.validated_data['food_level_low']
            feeder_status.save()

            return Response({'message': 'Food Level Updated Successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
        