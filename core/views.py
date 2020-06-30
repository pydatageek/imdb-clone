from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, TemplateView

from celebs.helpers import (
    get_latest_celebs, get_featured_celebs, get_random_celebs)
from celebs.models import Celebrity, Duty
from movies.helpers import (
    get_latest_movies, get_featured_movies, get_random_movies)
from movies.models import Genre, Movie, PgRating
"""
# TODO: this part is for fast search with postgreSQL.search

from django.contrib.postgres.search import SearchQuery, SearchRank
from django.db.models import F, Q
"""


class Home(TemplateView):
    """Homepage return featured & latest movies, celebs"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title'] = _('IMDB Clone')

        # movies context
        context['featured_movies'] = get_featured_movies(8)
        # context['latest_movies'] = get_latest_movies(13)
        # context['random_movies'] = get_random_movies()

        # celebrities context
        context['featured_celebs'] = get_featured_celebs(3)
        # context['latest_celebs'] = get_latest_celebs(13)
        # context['random_celebs'] = get_random_celebs()

        # # movies + celebrities context
        # context['featured_items'] = [context['featured_movies'],
        #                              context['featured_celebs']]
        # context['latest_items'] = [context['latest_movies'],
        #                            context['latest_celebs']]
        # context['random_items'] = [context['random_movies'],
        #                            context['random_celebs']]

        return context


class Search(ListView):
    model = Movie

    def get_context_data(self, *args, **kwargs):
        query = str(self.request.GET.get('q')).strip()

        context = super().get_context_data(*args, **kwargs)

        context['q'] = query
        context['title'] = _('Search')
        context['title_page_suffix'] = query
        context['movies_title'] = _('Movies')
        context['movies'] = Movie.objects.filter(name__icontains=query)
        context['celebs_title'] = _('Celebrities')
        context['celebs'] = Celebrity.objects.filter(
            name__icontains=query)

        context['duties'] = Duty.objects.filter(name__icontains=query)
        context['genres'] = Genre.objects.filter(name__icontains=query)
        context['pg_ratings'] = PgRating.objects.filter(
            name__icontains=query)

        """
        # TODO: this part is for fast search with postgreSQL.search

        context['movies'] = Movie.objects.annotate(rank=SearchRank(
            F('name_vector'), SearchQuery(query))).filter(
                rank__gt=0.0).order_by('-rank')
        context['celebs'] = Celebrity.objects.annotate(rank=SearchRank(
            F('name_vector'), SearchQuery(query))).filter(
                rank__gt=0.0).order_by('-rank')
        """

        context['random_movies'] = get_random_movies(3)
        context['random_celebs'] = get_random_celebs(3)

        return context
