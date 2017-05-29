from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.


class Date(models.Model):
    """
    Model for date objects.
    """
    date_id = models.AutoField(primary_key=True)
    release_year = models.CharField(max_length=4)

    def __str__(self):
        return self.release_year

    def validate_year(self):
        """
        validate that the input to the database is a legitimate year. 
        """
        try:
            datetime.datetime.strptime(self.release_year, '%Y')
        except Exception as e:
            # In main function, do not save object to the database.
            pass


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






