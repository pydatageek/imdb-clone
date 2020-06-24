from django.urls import include, path

from .views import (
    GenreDetail, GenresList, MovieDetail, MoviesList,
    PgRatingDetail, PgRatingsList)

base_dir = 'vue/'

urlpatterns = [
    path('genre', include([
        path('<slug:slug>/', GenreDetail.as_view(
            template_name=base_dir + 'movies/genre_detail.html'
        ), name='genre_detail'),
        path('', GenresList.as_view(
            template_name=base_dir + 'movies/genre_list.html'
        ), name='genre_list')
    ])),
    path('pg-rating', include([
        path('<slug:slug>/', PgRatingDetail.as_view(
            template_name=base_dir + 'movies/pg_rating_detail.html'
        ), name='pg-rating-detail'),
        path('', PgRatingsList.as_view(
            template_name=base_dir + 'movies/pg_rating_list.html'
        ), name='pg_rating_list')
    ])),
    path('', include([
        path('<slug:slug>/', MovieDetail.as_view(
            template_name=base_dir + 'movies/movie_detail.html'
        ), name='movie_detail'),
        path('', MoviesList.as_view(
            template_name=base_dir + 'movies/movie_list.html'
        ), name='movie_list')
    ])),
]
