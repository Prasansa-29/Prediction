from django.db import models
    
class Patient(models.Model):
    age = models.IntegerField()
    sex = models.BooleanField(default=False)  # True for Male, False for Female
    chest_pain = models.IntegerField()
    resting_blood_pressure = models.IntegerField()
    cholesterol = models.IntegerField()
    fasting_blood_sugar = models.IntegerField()
    max_heart_rate = models.IntegerField()
    
   