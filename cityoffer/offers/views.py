from django.shortcuts import render

from django.http import HttpResponse
from .models import Offer

def index(request):
	return HttpResponse("hello") 

# Create your views here.