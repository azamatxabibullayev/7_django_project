from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def bmw(request):
    return HttpResponse('THIS PAGE IS ONLY FOR BMW !!!!!')
