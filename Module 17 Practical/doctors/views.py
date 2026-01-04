from rest_framework import generics
from django.shortcuts import render
from .models import Doctor
from .serializers import DoctorSerializer

# Create your views here.
class DoctorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Doctor.objects.filter(is_active = True)
    serializer_class = DoctorSerializer

class DoctorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer