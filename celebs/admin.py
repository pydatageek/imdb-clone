from django.db.models import Count, TextField
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from imagekit.admin import AdminThumbnail
from import_export.admin import ImportExportModelAdmin

from core.admin import BaseAdmin
from core.imagegenerators import cached_list_thumb
from .forms import CelebrityForm
from .models import Duty, Celebrity
from .resources import DutyResource, CelebrityResource


@admin.register(Duty)
class DutyAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = DutyResource

    save_on_top = True
    search_fields = ('name',)

    ordering = ('code',)
    list_display = ('name', 'code', 'celebs_count', 'slug')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_celebs_count=Count('celebs', distinct=True))

    def celebs_count(self, obj):
        return obj._celebs_count
    celebs_count.short_description = _('# Celebs')
    celebs_count.admin_order_field = '_celebs_count'


@admin.register(Celebrity)
class CelebrityAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = CelebrityResource
    form = CelebrityForm

    save_on_top = True
    list_filter = ('duties',)
    search_fields = ('first_name', 'last_name', 'duties__name')

    ordering = ('last_name', 'first_name')
    list_display = (
        'admin_thumbnail', 'first_name', 'last_name',
        'is_featured', 'slug',
        'age', 'updated_at')
    list_display_links = ('first_name', 'last_name')
    list_editable = ('is_featured',)

    admin_thumbnail = AdminThumbnail(image_field=cached_list_thumb)

    readonly_fields = (
        'name', 'slug', 'extra_chars_count', 'admin_thumbnail',
        'added_by', 'added_at', 'updated_by', 'updated_at')
    fieldsets = (
        (_('Info'), {
            'fields': (
                ('name', 'slug'), ('first_name', 'last_name'),
                ('nick_name', 'is_featured'),
                ('birthdate', 'birth_place'),
                ('deathdate', 'death_place'),
                'content', 'content_source',
                'trailer', 'trailer_info',
                ('admin_thumbnail', 'image'), 'image_credit',
                'duties', 'imdb_id'
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
