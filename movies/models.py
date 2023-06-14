"""
Models for Movie Database.

This module defines the Django models for the Movie Database application. It includes
the Genre and Movie models representing movie genres and individual movies, respectively.

Dependencies:
    - Django (version 4.2.2)

Note:
    This module requires a working Django installation and database connection.

Usage Example:
    # Import models
    from movie.models import Genre, Movie

    # Create a genre
    genre = Genre(name='Action')
    genre.save()

    # Create a movie
    movie = Movie(title='Inception', release_year=2010, number_in_stock=10, daily_rate=2.99, genre=genre)
    movie.save()
"""
from django.db import models
from django.utils import timezone


class Genre(models.Model):
    """A model representing a movie genre.

    Attributes:
        name (str): The name of the genre.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """A model representing a movie.

    Attributes:
        title (str): The title of the movie.
        release_year (int): The year the movie was released.
        number_in_stock (int): The number of copies of the movie available in stock.
        daily_rate (float): The rental rate per day for the movie.
        genre (Genre): The genre of the movie (foreign key to the Genre model).
        date_created (datetime): The date and time when the movie record was created.
    """
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
