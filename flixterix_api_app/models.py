from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Date(models.Model):
    """
    Model for date objects.
    """
    date_id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=4)

    def __str__(self):
        return self.release_year


class Genre(models.Model):
    """
    Model for genre objects. 
    """
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """
    Model for movie objects. 
    """
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.ForeignKey(Date)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title






