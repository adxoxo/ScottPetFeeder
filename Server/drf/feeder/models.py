from django.db import models

# Create your models here.
class FeederStatus(models.Model):
    is_manual_mode = models.BooleanField(default=False)
    food_level_low = models.BooleanField(default=False)
    
    def __str__(self):
        return "Manual Mode: {}, Food Level Low: {}".format(self.is_manual_mode, self.food_level_low)