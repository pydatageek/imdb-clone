"""simple base viewsets"""
from django.db.models import Prefetch

from rest_framework import viewsets

from movies.models import Genre, Movie, PgRating
from .serializers import GenreSerializer, MovieSerializer, PgRatingSerializer


class GenreApiViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.prefetch_related(
        Prefetch('movies', Movie.objects.only('id'))
    )
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    # permission_classes =


class MovieApiViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.select_related('pg_rating').prefetch_related(
        'genres', 'crews')
    serializer_class = MovieSerializer
    lookup_field = 'slug'
    # permission_classes =
    # reverse_action =


class PgRatingApiViewSet(viewsets.ModelViewSet):
    queryset = PgRating.objects.prefetch_related(
        Prefetch('movies', Movie.objects.only('id'))
    )
    serializer_class = PgRatingSerializer
    lookup_field = 'slug'
    # permission_classes =
