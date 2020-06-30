from django.urls import include, path

from .views import (
    GenreDetailView, GenreListView, MovieDetailView, MovieListView, TopMovieListView,
    PgRatingDetailView, PgRatingListView)

base_dir = 'html/lte/'

urlpatterns = [
    path('genre/', include([
        path('<slug:slug>/', GenreDetailView.as_view(
            template_name=base_dir + 'movies/genre_detail.html'
        ), name='genre-detail'),
        path('', GenreListView.as_view(
            template_name=base_dir + 'movies/genre_list.html'
        ), name='genre-list')
    ])),
    path('pg-rating/', include([
        path('<slug:slug>/', PgRatingDetailView.as_view(
            template_name=base_dir + 'movies/pg_rating_detail.html'
        ), name='pg-rating-detail'),
        path('', PgRatingListView.as_view(
            template_name=base_dir + 'movies/pg_rating_list.html'
        ), name='pg-rating-list')
    ])),
    path('', include([
        path('top/', TopMovieListView.as_view(
            template_name=base_dir + 'movies/movie_list.html'
        ), name='top-movie-list'),
        path('<slug:slug>/', MovieDetailView.as_view(
            template_name=base_dir + 'movies/movie_detail.html'
        ), name='movie-detail'),
        path('', MovieListView.as_view(
            template_name=base_dir + 'movies/movie_list.html'
        ), name='movie-list')
    ])),
]
