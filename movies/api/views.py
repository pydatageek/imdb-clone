"""simple base viewsets"""
from rest_framework import viewsets

from movies.models import Genre, Movie, PgRating
from .serializers import GenreSerializer, MovieSerializer, PgRatingSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related(
        'genres', 'crews')
    serializer_class = MovieSerializer


class PgRatingViewsSet(viewsets.ModelViewSet):
    queryset = PgRating.objects.all()
    serializer_class = PgRatingSerializer
