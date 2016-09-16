from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hell World, you are at the poll index.")
# Create your views here.
