from rest_framework import serializers
from HeartDisease.models import Patient

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    patient_id = serializers.ReadOnlyField()
    class Meta:
        model= Patient
        fields= "__all__"
