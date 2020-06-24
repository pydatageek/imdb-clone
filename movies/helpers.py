import random
from random import shuffle

from django.db.models import Q, Max

from .models import Movie

number_of_items = 5


def no_objects_exists():
    """checks whether db table has any objects recorded.
    if there is no object, it will return an empty list []"""
    if not Movie.objects.all().exists():
        return []


def get_movies_queryset():
    """retrieves the objects' queryset ordered by '-added_at' (defined on model) 
    which is sorted as latest added first."""
    return Movie.objects.all()


def get_movies_list():
    """some functions need a list rather than a queryset."""
    return list(get_movies_queryset())


def get_latest_movies(num=number_of_items):
    """retrieves latest added movies from db if there is any 
    (because default order on model is '-added_at')"""

    no_objects_exists()

    return get_movies_list()[:num]


def get_featured_movies(num=number_of_items):
    """retrieves featured movies from db if there is any.
    is_featured is a field in the model. also the featured item should have 
    either trailer or image"""

    no_objects_exists()

    featured = get_movies_queryset().filter(
        Q(is_featured=True) & (
            Q(trailer__isnull=False) | Q(image__isnull=False)))
    if featured.exists():
        featured = list(featured)  # make featured queryset a list
        shuffle(featured)  # make the list randomly ordered
        return featured[:num]
    else:
        return get_latest_movies(num)


def get_random_movies(num=number_of_items):
    """retrieves 'num' number of random movies."""

    no_objects_exists()

    movies = get_movies_list()  # list in order to shuffle
    shuffle(movies)  # make the list randomly ordered
    return movies[:num]
