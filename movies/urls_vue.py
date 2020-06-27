from django.urls import include, path

from .views import (
    GenreDetail, GenreList, MovieDetail, MovieList,
    PgRatingDetail, PgRatingList)

base_dir = 'vue/'

urlpatterns = [
    path('genre', include([
        path('<slug:slug>/', GenreDetail.as_view(
            template_name=base_dir + 'movies/genre_detail.html'
        ), name='genre-detail'),
        path('', GenreList.as_view(
            template_name=base_dir + 'movies/genre_list.html'
        ), name='genre-list')
    ])),
    path('pg-rating', include([
        path('<slug:slug>/', PgRatingDetail.as_view(
            template_name=base_dir + 'movies/pg_rating_detail.html'
        ), name='pg-rating-detail'),
        path('', PgRatingList.as_view(
            template_name=base_dir + 'movies/pg_rating_list.html'
        ), name='pg-rating-list')
    ])),
    path('', include([
        path('<slug:slug>/', MovieDetail.as_view(
            template_name=base_dir + 'movies/movie_detail.html'
        ), name='movie-detail'),
        path('', MovieList.as_view(
            template_name=base_dir + 'movies/movie_list.html'
        ), name='movie-list')
    ])),
]
