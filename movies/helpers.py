import random
from random import shuffle

from django.db.models import Q, Max

from .models import Movie

number_of_items = 5


def no_objects_exists():
    """Checks whether db table has any objects recorded.
    If there is no object, it will return an empty list []
    """
    if not Movie.objects.exists():
        return []


def get_movies_queryset():
    """Retrieves the objects' queryset."""
    return Movie.objects.select_related(
        'pg_rating').prefetch_related('genres').only(
            'slug', 'name', 'image', 'release_date', 'imdb_rating',
            'duration', 'pg_rating')


def get_movies_list():
    """Some functions need a list rather than a queryset."""
    return list(get_movies_queryset())


def get_movies_queryset_limited():
    """Retrieves the objects' queryset."""
    return Movie.objects.only('slug', 'name', 'image')


def get_movies_list_limited():
    """Some functions need a list rather than a queryset."""
    return list(get_movies_queryset_limited())


def get_latest_movies(num=number_of_items):
    """Retrieves latest added movies from db if there is any."""
    # no_objects_exists()

    return get_movies_list()[:num]


def get_featured_movies(num=number_of_items):
    """Retrieves featured movies from db if there is any.
    is_featured is a field in the model. also the featured item should 
    have either trailer or image
    """
    # no_objects_exists()

    featured = get_movies_queryset().filter(
        Q(is_featured=True) & (
            Q(trailer__isnull=False) | Q(image__isnull=False)))
    if len(featured):
        featured = list(featured)  # make featured queryset a list
        shuffle(featured)  # make the list randomly ordered
        return featured[:num]
    else:
        return get_latest_movies(num)


def get_random_movies(num=number_of_items):
    """Retrieves 'num' number of random movies."""
    # no_objects_exists()

    movies = get_movies_list()  # list in order to shuffle
    shuffle(movies)  # make the list randomly ordered
    return movies[:num]


def get_random_movies_limited(num=number_of_items):
    """Retrieves 'num' number of random movies."""
    # no_objects_exists()

    movies = get_movies_list_limited()  # list in order to shuffle
    shuffle(movies)  # make the list randomly ordered
    return movies[:num]
