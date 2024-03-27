from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('age', 'sex','chest_pain', 'resting_blood_pressure', 'cholesterol', 'fasting_blood_sugar', 'max_heart_rate' )
    
    
    
admin.site.register(Patient, PatientAdmin)