from django.db.models import Count
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView

from movies.helpers import get_random_movies
from .models import Duty, Celebrity
from .helpers import get_random_celebs


class CelebDetail(DetailView):
    model = Celebrity

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        context['random_celebs'] = get_random_celebs()
        context['random_movies'] = get_random_movies()
        return context


class CelebList(ListView):
    model = Celebrity

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Celebrities')
        context['random_celebs'] = get_random_celebs()
        context['random_movies'] = get_random_movies()
        return context


class DutyDetail(DetailView):
    model = Duty

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        context['title_page_prefix'] = _('Celebrity Duty')
        context['celebs'] = Celebrity.objects.prefetch_related(
            'duties').filter(duties__pk=self.get_object().pk)
        context['random_celebs'] = get_random_celebs()
        context['random_movies'] = get_random_movies()
        return context


class DutyList(ListView):
    model = Duty

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.annotate(celebs_count=Count('celebs', distinct=True))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Celebrity Duties')
        context['description'] = _("Celebrities' duties in movies or shows \
            are listed below.")
        context['random_celebs'] = get_random_celebs()
        context['random_movies'] = get_random_movies()
        return context
