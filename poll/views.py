from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hell World, you are at the poll index.")
# Create your views here.

def vote(request, ballot_id):
    return HttpResponse("You're looking at ballot %s." % str(ballot_id))

def result(request, ballot_id):
     response = "You're looking at the results of the election %s."
     return HttpResponse(response % str(ballot_id))
