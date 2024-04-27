from django.urls import path
from bmw.views import bmw

urlpatterns = [
    path('bmw', bmw)
]
