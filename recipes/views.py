from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# HTTP REQUEST
def home(request):
    return HttpResponse("Home")
    # return HTTP Response


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponse("Contact")
  