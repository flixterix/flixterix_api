"""
Serializers for storing data into JSON format. 
"""

from flixterix_api_app.models import Date, Genre, Movie

from rest_framework import serializers


class DateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Date
        fields = ('release_year')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name')


class MovieSerializer(serializers.ModelSerializer):

    genres = serializers.StringRelatedField(many=True)
    # date = serializers.SlugRelatedField(slug_field='release_year')

    class Meta:
        model = Movie
        fields = ('title', 'genres', 'date')

