from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('This is home page')

def room(request):
    return HttpResponse('This is room page')