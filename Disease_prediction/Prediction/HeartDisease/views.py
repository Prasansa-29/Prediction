from django.shortcuts import render, redirect
from rest_framework import viewsets
from HeartDisease.models import Patient
from HeartDisease.serializers import PatientSerializer
from rest_framework.decorators import action 
from rest_framework.response import Response
from HeartDisease.algorithm import build_tree, predict


class PatientViewSet(viewsets.ModelViewSet):
    queryset= Patient.objects.all()
    serializer_class= PatientSerializer
    
    
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            predict=Patient.objects.get(pk=pk)
            predict_serializer=PatientSerializer(predict, many=True,context={'request', request} )
            return Response(predict_serializer.data)
        except Exception as e:
            print(e)
            return ResourceWarning({
                'message': 'The data might not exist'
            })
            
            
def train_model(request):
    patients = Patient.objects.all().values()
    features = [field.name for field in Patient._meta.get_fields() if field.name != 'has_heart_disease']
    tree = build_tree(list(patients), features)
    # You can save the tree to use it later for predictions
    return render(request, 'train_model.html')

def make_prediction(request):
    # Get patient data from request
    patient_data = {
        'age': request.POST['age'],
        'sex': request.POST['sex'],
        # Add other features accordingly
    }
    # Make prediction
    prediction = predict(tree, patient_data)
    return render(request, 'prediction_result.html', {'prediction': prediction})