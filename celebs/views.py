from django.db.models import Count, Prefetch
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView

from movies.helpers import get_random_movies, get_random_movies_limited
from movies.models import Movie
from .models import Celebrity, Duty
from .helpers import get_random_celebs


class CelebDetailView(DetailView):
    model = Celebrity

    def get_queryset(self):
        qs = super().get_queryset().prefetch_related(
            'moviecrews',
            Prefetch(
                'moviecrews__movie', Movie.objects.only('name', 'slug')),
            Prefetch('moviecrews__duty', Duty.objects.only('name')))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        context['title_alt'] = _('Celebrity')
        context['random_celebs'] = get_random_celebs(3)
        context['random_movies'] = get_random_movies_limited(3)
        return context


class CelebListView(ListView):
    model = Celebrity

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Celebrities')
        context['random_celebs'] = get_random_celebs(3)
        context['random_movies'] = get_random_movies_limited(3)
        return context


class DutyDetailView(DetailView):
    model = Duty

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        context['title_alt'] = _('Celebrity Duty')
        context['title_page_prefix'] = _('Celebrity Duty')
        context['celebs'] = Celebrity.objects.prefetch_related(
            Prefetch('duties', Duty.objects.only('pk'))).only(
            'slug', 'name', 'first_name', 'last_name', 'image',
            'birthdate', 'deathdate').filter(
                duties__pk=self.get_object().pk)
        context['random_celebs'] = get_random_celebs(3)
        context['random_movies'] = get_random_movies_limited(3)
        return context


class DutyListView(ListView):
    model = Duty

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs).values(
            'name', 'slug', 'code').annotate(
                celebs_count=Count('celebs'))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Celebrity Duties')
        context['description'] = _(
            "Celebrities' duties in movies or shows are listed below.")
        context['random_celebs'] = get_random_celebs(3)
        context['random_movies'] = get_random_movies_limited(3)
        return context
