from django.urls import path, include
from HeartDisease.views import PatientViewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'Patients', PatientViewSet)

urlpatterns = [ 
path('',include(router.urls) )
]
