from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, routers
from .models import Date, Genre, Movie
from .serializers import DateSerializer, GenreSerializer, MovieSerializer



# Create your views here.

# List all dates or creates a new one.

class DateViewSet(APIView):
    """
    API Responses dealing with date objects. 
    """

    def get(self, request):
        dates = Date.objects.all()
        serializer = DateSerializer(dates, many=True)
        return Response(serializer.data)


    def post(self):
        pass


class GenreViewSet(APIView):
    """
    API Responses dealing with genre objects
    """

    def get(self):
        pass


    def post(self):
        pass


class MovieViewSet(APIView):
    """
    API responses dealing with movie objects. 
    """

    def get(self):
        pass

    def post(self):
        pass

