from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Movies
class Movies(models.Model):
    """
    Model for movie objects. 
    """
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    release_year = models.ForeignKey(Date, max_length=4)

    def __str__(self):
        return self.title


class Genres(models.Model):
    """
    Model for genre objects. 
    """
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Date(models.Model):
    """
    Model for date objects.
    """