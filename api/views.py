from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import BehaviorLog
from .serializer import BehaviorLogSerializer

# Create your views here.
class BehaviorLogViewSet(viewsets.ModelViewSet):
    queryset = BehaviorLog.objects.all()
    serializer_class = BehaviorLogSerializer
