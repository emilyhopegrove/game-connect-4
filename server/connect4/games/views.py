# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Connect 4 Game!")   

def about(request):
    return HttpResponse("This is the About page for the Connect 4 Game.")