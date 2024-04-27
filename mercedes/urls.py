from django.urls import path
from mercedes.views import mercedes

urlpatterns = [
    path('mercedes', mercedes)
]
