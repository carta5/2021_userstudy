from django.urls import path

from rest_framework import routers
from .views import BehaviorLogViewSet

router = routers.DefaultRouter()
router.register(r'behaviors', BehaviorLogViewSet)
