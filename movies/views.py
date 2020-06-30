from django.db.models import Count, Prefetch
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView

from celebs.helpers import get_random_celebs
from celebs.models import Celebrity, Duty
from .models import Genre, Movie, PgRating
from .helpers import get_random_movies, get_random_movies_limited


class GenreDetailView(DetailView):
    model = Genre

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        context['title_alt'] = _('Genre')
        context['title_page_prefix'] = _('Genre')
        context['movies'] = Movie.objects.only(
            'name', 'slug', 'image', 'imdb_rating',
            'duration', 'release_date').filter(
                genres__id=self.get_object().id)
        context['random_celebs'] = get_random_celebs(3)
        context['random_movies'] = get_random_movies_limited(3)
        return context


class GenreListView(ListView):
    model = Genre

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs).values(
            'name', 'slug', 'code').annotate(
            movies_count=Count('movies__id'))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Genres')
        context['description'] = _(
            'Movie genres used to categorize movies \
            on this wesite is listed below.')
        context['random_celebs'] = get_random_celebs(3)
        context['random_movies'] = get_random_movies_limited(3)
        return context


class MovieDetailView(DetailView):
    model = Movie

    def get_queryset(self):
        qs = super().get_queryset().select_related(
            'pg_rating').prefetch_related(
                Prefetch('genres', Genre.objects.only('name', 'slug')),
                Prefetch('moviecrews__duty', Duty.objects.only('name')),
                Prefetch(
                    'moviecrews__crew',
                    Celebrity.objects.only('name', 'slug', 'image')))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        context['title_alt'] = _('Movie')
        context['random_celebs'] = get_random_celebs(3)
        context['random_movies'] = get_random_movies_limited(3)
        return context


class MovieListView(ListView):
    model = Movie

    def get_queryset(self):
        qs = super().get_queryset().only(
            'slug', 'name', 'image', 'release_date',
            'imdb_rating', 'duration')
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Movies')
        context['random_celebs'] = get_random_celebs(3)
        context['random_movies'] = get_random_movies_limited(3)
        return context


class TopMovieListView(ListView):
    model = Movie

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('imdb_rating')
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Top Movies')
        context['description'] = _('Top Rated Movies of IMDB')
        context['random_celebs'] = get_random_celebs(3)
        context['random_movies'] = get_random_movies_limited(3)
        return context


class PgRatingDetailView(DetailView):
    model = PgRating

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        context['title_alt'] = _('PG Rating')
        context['title_page_prefix'] = _('PG Rating')
        context['movies'] = Movie.objects.only(
            'name', 'slug', 'image', 'imdb_rating',
            'duration', 'release_date').filter(
                pg_rating__id=self.get_object().id)
        context['random_celebs'] = get_random_celebs(3)
        context['random_movies'] = get_random_movies_limited(3)
        return context


class PgRatingListView(ListView):
    model = PgRating

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs).values(
            'name', 'slug', 'code', 'content').annotate(
                movies_count=Count('movies'))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Parental Guidance (PG) Ratings')
        context['description'] = _(
            'Motion picture content & TV content \
            is rated with Parental Guidance (PG) rating system.')
        context['random_celebs'] = get_random_celebs(3)
        context['random_movies'] = get_random_movies_limited(3)
        return context
