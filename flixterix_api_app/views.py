from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """
    Index base page.
    """
    return HttpResponse("Hello world. Welcome to the best movie API ever.")
