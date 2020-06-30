"""Models related with Celebrities e.g. Celebrity, Duty"""

from datetime import date

from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Count
from django.urls import reverse
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

from core.models import NameSlugStampedModel
from core.helpers import (
    get_age, get_extension, random_chars, video_code)
"""
# TODO: this part is for fast search with postgreSQL.search

from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
"""


def celeb_directory_path(instance, filename):
    """The computed upload folder for celebrity images"""
    file_and_ext = get_extension(filename)
    return f'celebs/{instance.id}/{file_and_ext[0].lower()} \
        -{random_chars(5)}{file_and_ext[1]}'


class Duty(NameSlugStampedModel):
    """duty of celebs"""
    code = models.CharField(
        _('code'), max_length=2, db_index=True)

    extra_chars_count = models.PositiveSmallIntegerField(
        _('extra characters count'), default=0, editable=False,
        help_text=_('there is no need for extra chars for slug of \
        this model and if no need for it to be editable also.'))

    class Meta:
        verbose_name = _('duty')
        verbose_name_plural = _('duties')

    def get_absolute_url(self):
        return reverse('duty-detail', args=[self.slug])


class Celebrity(NameSlugStampedModel):
    """Celebrity model
    TODO: birthdate <= today, deathdate <= today and 
    birthdate < deathdate checks
    """
    # name field is overriden
    name = models.CharField(
        _('full name'), max_length=245, unique=False, db_index=True,
        blank=True, editable=False, help_text=_('computed full name'))
    birth_name = models.CharField(
        _('birth name'), max_length=245, blank=True)

    first_name = models.CharField(
        _('first name'), max_length=75)
    last_name = models.CharField(
        _('last name'), max_length=75, default='', blank=True)
    nick_name = models.CharField(
        _('nick name'), max_length=50, default='', blank=True)

    is_featured = models.BooleanField(
        _('featured'), default=False)

    imdb_id = models.CharField(
        _('IMDB Id'), max_length=15, default='', blank=True,
        db_index=True)  # db_index is True for massive imports

    # TODO:
    # starmeter_rating = models.FloatField(
    #     _('StarMeter rating'), default=0, blank=True,
    #     help_text=_('e.g. 6.8'))

    birthdate = models.DateField(
        _('birth date'), blank=True, null=True)
    # TODO: MayBe: birth_place be country, state, city, town
    birth_place = models.CharField(
        _('birth place'), max_length=200, default='', blank=True)
    deathdate = models.DateField(
        _('death date'), blank=True, null=True)
    # TODO: MayBe: death_place be country, state, city, town
    death_place = models.CharField(
        _('death place'), max_length=200, default='', blank=True)
    death_reason = models.CharField(
        _('death reason'), max_length=255, default='', blank=True)

    content = RichTextField(
        _('biography'), default='', blank=True)
    # TODO: MayBe: content_source be transformed into an MTM
    # or Text field
    content_source = models.URLField(
        _('content source'), default='', blank=True)

    trailer = models.URLField(
        _('trailer'), default='', blank=True,
        help_text=_('trailer url (ONLY for youtube videos yet)'))
    trailer_info = models.CharField(
        _('trailer info'), max_length=250, default='', blank=True)

    image = models.ImageField(
        _('image'), upload_to=celeb_directory_path,
        blank=True, null=True)
    image_credit = models.CharField(
        _('image credit'), max_length=250, default='', blank=True)

    duties = models.ManyToManyField(
        Duty, blank=True,
        related_name='celebs', verbose_name=_('duties'),
        help_text=_("Celebrities' duties in movies"))

    """
    # TODO: this part is for fast search with postgreSQL.search

    first_name_vector = SearchVectorField(null=True)
    last_name_vector = SearchVectorField(null=True)
    """

    @cached_property
    def age(self):
        return get_age(self.birthdate, self.deathdate)

    @cached_property
    def trailer_video(self):
        return video_code(self.trailer)

    @property
    def as_producer(self):
        return self._get_movie('P')

    @property
    def as_director(self):
        return self._get_movie('D')

    @property
    def as_writer(self):
        return self._get_movie('W')

    @property
    def as_cast(self):
        return self._get_movie('C')

    class Meta:
        verbose_name = _('celebrity')
        verbose_name_plural = _('celebrities')

        """
        # TODO: this part is for fast search with postgreSQL.search

        indexes = [GinIndex(fields=[
            'first_name_vector',
            'last_name_vector',
        ])]
        """

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = f'{self.first_name} {self.last_name}'
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('celeb-detail', args=[self.slug])

    def _get_movie(self, duty_code):
        if hasattr(self, '_prefetched_objects_cache') and 'moviecrews' in self._prefetched_objects_cache:
            return [c for c in self._prefetched_objects_cache['moviecrews'] if c.duty.code == duty_code]
        else:
            return self.moviecrews.filter(duty__code=duty_code)
