from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from celebs.helpers import (
    get_latest_celebs, get_featured_celebs, get_random_celebs)
from movies.helpers import (
    get_latest_movies, get_featured_movies, get_random_movies)


class Home(TemplateView):
    """Homepage return featured & latest movies, celebs"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title'] = _('IMDB Clone')

        # movies context
        context['featured_movies'] = get_featured_movies(8)
        context['latest_movies'] = get_latest_movies(13)
        context['random_movies'] = get_random_movies()

        # celebrities context
        context['featured_celebs'] = get_featured_celebs(8)
        context['latest_celebs'] = get_latest_celebs(13)
        context['random_celebs'] = get_random_celebs()

        # movies + celebrities context
        context['featured_items'] = [context['featured_movies'],
                                     context['featured_celebs']]
        context['latest_items'] = [context['latest_movies'],
                                   context['latest_celebs']]
        context['random_items'] = [context['random_movies'],
                                   context['random_celebs']]

        return context
