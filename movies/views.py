from django.db.models import Count, Prefetch
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView

from celebs.helpers import get_random_celebs
from celebs.models import Celebrity, Duty
from .models import Genre, Movie, PgRating
from .helpers import get_random_movies, get_random_movies_limited


class GenreDetail(DetailView):
    model = Genre

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        context['title_alt'] = _('Genre')
        context['title_page_prefix'] = _('Genre')
        context['movies'] = Movie.objects.prefetch_related('genres').filter(
            genres__id=self.get_object().id)
        context['random_celebs'] = get_random_celebs()
        context['random_movies'] = get_random_movies_limited()
        return context


class GenreList(ListView):
    model = Genre

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs).annotate(
            movies_count=Count('movies'))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Genres')
        context['description'] = _('Movie genres used to categorize movies \
            on this wesite is listed below.')
        context['random_celebs'] = get_random_celebs(3)
        context['random_movies'] = get_random_movies_limited(3)
        return context


class MovieDetail(DetailView):
    model = Movie

    def get_queryset(self):
        qs = super().get_queryset().select_related(
            'pg_rating').prefetch_related(
                'genres', 'moviecrews__duty', 'moviecrews__crew')
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        context['title_alt'] = _('Movie')
        context['random_celebs'] = get_random_celebs()
        context['random_movies'] = get_random_movies_limited()
        return context


class MovieList(ListView):
    model = Movie

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Movies')
        context['random_celebs'] = get_random_celebs()
        context['random_movies'] = get_random_movies_limited()
        return context


class TopMovieList(ListView):
    model = Movie

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('imdb_rating')
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Top Movies')
        context['description'] = _('Top Rated Movies of IMDB')
        context['random_celebs'] = get_random_celebs()
        context['random_movies'] = get_random_movies_limited()
        return context


class PgRatingDetail(DetailView):
    model = PgRating

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        context['title_alt'] = _('PG Rating')
        context['title_page_prefix'] = _('PG Rating')
        context['movies'] = Movie.objects.select_related('pg_rating').filter(
            pg_rating__id=self.get_object().id)
        context['random_celebs'] = get_random_celebs()
        context['random_movies'] = get_random_movies_limited()
        return context


class PgRatingList(ListView):
    model = PgRating

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.annotate(movies_count=Count('movies'))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Parental Guidance (PG) Ratings')
        context['description'] = _('Motion picture content & TV content \
            is rated with Parental Guidance (PG) rating system.')
        context['random_celebs'] = get_random_celebs()
        context['random_movies'] = get_random_movies_limited()
        return context
