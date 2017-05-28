from django.contrib import admin

from .models import Movie, Genre, Date
# Register your models here.

# add and delete movies, genres and dates.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Date)

