from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def mercedes(request):
    return HttpResponse('THIS PAGE ONLY FOR MERCEDES !')
