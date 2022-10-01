from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world, You're at the polls index")
# Create your views here.
