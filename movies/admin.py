from django.db.models import Count, TextField
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from imagekit.admin import AdminThumbnail
from import_export.admin import ImportExportModelAdmin

from core.admin import BaseAdmin
from core.imagegenerators import cached_list_thumb
from .forms import GenreForm, PgRatingForm
from .models import Genre, PgRating, Movie, MovieCrew
from .resources import (
    GenreResource, PgRatingResource, MovieResource, MovieCrewResource)


class MovieCrewInline(admin.TabularInline):
    model = MovieCrew
    autocomplete_fields = ('crew',)


@admin.register(Genre)
class GenreAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = GenreResource
    form = GenreForm

    save_on_top = True
    search_fields = ('name',)

    ordering = ('name',)
    list_display = ('name', 'code', 'movies_count', 'slug')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_movies_count=Count('movies'))

    def movies_count(self, obj):
        return obj._movies_count
    movies_count.short_description = _('# Movies')
    movies_count.admin_order_field = '_movies_count'


@admin.register(PgRating)
class PgRatingAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = PgRatingResource
    form = PgRatingForm

    save_on_top = True
    search_fields = ('name', 'code')

    ordering = ('pk',)
    list_display = ('name', 'code', 'movies_count', 'slug')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_movies_count=Count('movies'))

    def movies_count(self, obj):
        return obj._movies_count
    movies_count.short_description = _('# Movies')
    movies_count.admin_order_field = '_movies_count'


@admin.register(Movie)
class MovieAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = MovieResource
    inlines = (MovieCrewInline,)

    save_on_top = True
    search_fields = ('name',)
    list_filter = ('pg_rating', 'imdb_rating')

    ordering = ('-added_at', '-release_date', 'name')
    list_display = (
        'admin_thumbnail', 'name', 'release_date', 'age',
        'is_featured', 'imdb_rating', 'duration', 'pg_rating')
    list_display_links = ('name',)
    list_editable = ('is_featured',)

    admin_thumbnail = AdminThumbnail(image_field=cached_list_thumb)

    readonly_fields = (
        'slug', 'extra_chars_count', 'admin_thumbnail',
        'added_by', 'added_at', 'updated_by', 'updated_at')
    autocomplete_fields = ('genres', 'pg_rating')
    fieldsets = (
        (_('Info'), {
            'fields': (
                ('name', 'slug'), 'original_name',
                ('release_date', 'duration'),
                ('imdb_id', 'imdb_rating', 'imdb_raters_count'),
                'content', 'content_source',
                'trailer', 'trailer_info',
                ('admin_thumbnail', 'image'), 'image_credit',
                'genres',
            )
        }),
        (_('Meta info'), {
            'classes': ('collapse',),
            'fields': (
                'extra_chars_count',
                ('added_by', 'added_at'), ('updated_by', 'updated_at'),
            )
        })
    )

    def age(self, obj):
        return obj.age
    age.admin_order_field = 'release_date'


@admin.register(MovieCrew)
class MovieCrew(ImportExportModelAdmin):
    resource_class = MovieCrewResource

    ordering = ('-movie__release_date', 'movie', 'list_order')
    list_display = ('crew', 'duty', 'role', 'movie')
