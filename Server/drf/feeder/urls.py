from django.urls import path
from .views import PetFeederView, PetFeederMobileView, MobileButtonView
urlpatterns = [
    path('status/', PetFeederView.as_view({
        'get':'manual_mode_view',
        'post':'food_level_view'
    })),
    
    path('mobile/', PetFeederMobileView.as_view({
        'get':'MobileFeederStatus',
        'post':'ManualModeSwitch'
    }))

    path('mobilebutton/', MobileButtonView.as_view({
        'post':'MobileDispense' 
    }))

    
]