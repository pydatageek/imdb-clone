"""Models related with Movies e.g. Movie, MovieCrew, Genre, PgRating"""

from django.core.validators import (
    ValidationError, MaxValueValidator, MinValueValidator)
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

from core.helpers import (
    get_age, get_duration_humanize, get_extension, random_chars, video_code)
from core.models import NameSlugStampedModel


def movie_directory_path(instance, filename):
    """The computed upload folder for movie images"""
    file_and_ext = get_extension(filename)
    return f'movies/{instance.id}/{file_and_ext[0].lower()} \
        -{random_chars(5)}{file_and_ext[1]}'


class Genre(NameSlugStampedModel):
    """movie genre model"""
    code = models.CharField(
        _('code'), max_length=3)
    content = models.CharField(
        _('content'), max_length=250, default='', blank=True)

    extra_chars_count = models.PositiveSmallIntegerField(
        _('extra characters count'), default=0, editable=False,
        help_text=_(
            'there is no need for extra chars for slug of this model \
            and if no need for it to be editable also.'))

    class Meta:
        verbose_name = _('genre')
        verbose_name_plural = _('genres')

    def get_absolute_url(self):
        return reverse('genre-detail', args=[self.slug])


class PgRating(NameSlugStampedModel):
    """parental guidance rating of movies"""
    code = models.CharField(
        _('code'), max_length=5)
    content = models.CharField(
        _('content'), max_length=250, default='', blank=True)

    extra_chars_count = models.PositiveSmallIntegerField(
        _('extra characters count'), default=0, editable=False,
        help_text=_(
            'there is no need for extra chars for slug of this model \
            and if no need for it to be editable also.'))

    class Meta:
        verbose_name = _('PG Rating')
        verbose_name_plural = _('PG Ratings')

    def __str__(self):
        return f'{self.code} ({self.name})'

    def get_absolute_url(self):
        return reverse('pgrating_detail', args=[self.slug])


class Movie(NameSlugStampedModel):
    """Movie model"""
    # name field is overriden
    name = models.CharField(
        _('title'), max_length=245, unique=True)
    original_name = models.CharField(
        _('original title'), max_length=245, default='', blank=True)

    is_featured = models.BooleanField(
        _('featured'), default=False)

    # TODO: retrieve release_year from release_date
    release_date = models.DateField(
        _('release date'), blank=True, null=True)

    # release_date = models.PositiveSmallIntegerField(
    #     _('release year'),
    #     validators=[MinValueValidator(1100), MaxValueValidator(2100)])

    duration = models.PositiveSmallIntegerField(
        _('duration'), default=0, blank=True, help_text=_('in minutes'))

    # country
    # language

    imdb_rating = models.FloatField(
        _('IMDB rating'), default=0, blank=True,
        validators=[
            MinValueValidator(0.0, message=_(
                'min. value cannot be negative')),
            MaxValueValidator(10.0, message=_(
                'max. value cannot be more then 10'))],
        help_text=_('e.g. 6.8'))
    imdb_raters_count = models.PositiveIntegerField(  # TODO: if rating 0, this should be 0 also
        _('IMDB raters count'), default=0, blank=True)
    imdb_id = models.CharField(
        _('IMDB Id'), max_length=15, default='', blank=True,
        db_index=True)  # db_index is True for massive imports

    # TODO:
    # rottentomatoes_rating = models.FloatField(
    #     _('RottenTomatoes rating'), default=0, blank=True,
    #     help_text=_('e.g. 6.8'))

    intro = models.TextField(
        _('intro'), default='', blank=True, max_length=500)
    content = RichTextField(
        _('content'), default='', blank=True)
    # TODO: MayBe: content_source be transformed into an MTM
    # or Text field
    content_source = models.URLField(
        _('content source'), default='', blank=True)
    # TODO: MayBe: an MTM for more trailers and BE for more
    # video sources
    trailer = models.URLField(
        _('trailer'), default='', blank=True,
        help_text=_('trailer url (ONLY for youtube videos yet)'))
    trailer_info = models.CharField(
        _('trailer info'), max_length=250, default='', blank=True)

    country = models.CharField(
        _('country'), max_length=100, default='', blank=True)
    language = models.CharField(
        _('language'), max_length=100, default='', blank=True)

    image = models.ImageField(
        _('image'), upload_to=movie_directory_path,
        blank=True, null=True)
    image_credit = models.CharField(
        _('image credit'), max_length=250, default='', blank=True)

    pg_rating = models.ForeignKey(
        PgRating, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='movies', verbose_name=_('PG rating'))

    genres = models.ManyToManyField(
        Genre, blank=True,
        related_name='movies', verbose_name=_('genre'))

    crews = models.ManyToManyField(
        'celebs.Celebrity', through='MovieCrew', blank=True,
        related_name='movies', verbose_name=_('crews'))

    @cached_property
    def age(self):
        return get_age(self.release_date)

    @cached_property
    def trailer_video(self):
        return video_code(self.trailer)

    @cached_property
    def duration_humanize(self):
        return get_duration_humanize(self.duration)

    @cached_property
    def release_year(self):
        return self.release_date.year

    @ property
    def producers(self):
        return self._get_crew('P')

    @ property
    def directors(self):
        return self._get_crew('D')

    @ property
    def writers(self):
        return self._get_crew('W')

    @ property
    def casts(self):
        return self._get_crew('C')

    @ property
    def all_crews(self):
        return self._get_crew('A')

    class Meta:
        verbose_name = _('movie')
        verbose_name_plural = _('movies')

    def get_absolute_url(self):
        return reverse('movie-detail', args=[self.slug])

    def clean(self, *args, **kwargs):
        if self.imdb_raters_count == 0 and self.imdb_rating != 0.0:
            raise ValidationError(
                _('With 0 raters, rating cannot be different than 0'))

    def _get_crew(self, duty_code='A'):
        """TODO: reduce queries"""
        result = []

        if duty_code == 'A':
            if hasattr(self, '_prefetched_objects_cache') \
                    and 'moviecrews' in self._prefetched_objects_cache:
                result = [
                    c for c in self._prefetched_objects_cache['moviecrews']]
            else:
                result = self.moviecrews.all()
            return result

        if hasattr(self, '_prefetched_objects_cache') \
                and 'moviecrews' in self._prefetched_objects_cache:
            result = [c for c in self._prefetched_objects_cache['moviecrews']
                      if c.duty.code == duty_code]
        else:
            result = self.moviecrews.filter(duty__code=duty_code)

        return result


class MovieCrew(models.Model):
    """m2m intermediate model for Movie and celebs.Celebrity models"""
    duty = models.ForeignKey(
        'celebs.Duty', on_delete=models.CASCADE, default=1,  # default is Cast
        related_name='moviecrews', verbose_name=_('duty'))

    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE,
        related_name='moviecrews', verbose_name=_('movie'))

    crew = models.ForeignKey(
        'celebs.Celebrity', on_delete=models.CASCADE,
        related_name='moviecrews', verbose_name=_('crew'))

    role = models.CharField(
        _('role'), max_length=75, default='', blank=True,
        help_text=_(
            'e.g. short story, screenplay for writer or voice for cast'))
    screen_name = models.CharField(
        _('screen name'), max_length=75, default='', blank=True,
        help_text=_("crew's name on movie"))

    list_order = models.PositiveSmallIntegerField(
        _('list order'), validators=[MinValueValidator(1)],
        help_text=_(
            'order of appearance on movie. normal appearance should \
            be producer(s) > director(s) > writer(s) > cast(s)'))

    class Meta:
        verbose_name = _('movie crew')
        verbose_name_plural = _('movie crews')
        unique_together = ('movie', 'list_order')

    def clean(self, *args, **kwargs):
        if not self.duty in self.crew.duties.all():
            raise ValidationError(
                _('crew duty and selected duty should match'),
                code='invalid')
        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.crew.name
