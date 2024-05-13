from django.urls import path
from .views import PetFeederView
urlpatterns = [
    path('status/', PetFeederView.as_view({
        'get':'manual_mode_view',
        'post':'food_level_view'
    }))
    
]