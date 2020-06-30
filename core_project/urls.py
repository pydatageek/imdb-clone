from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.views import Home, Search

html_dir = 'html/lte/'
jq_dir = 'jq/'
vue_dir = 'vue/'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ckeditor/', include('ckeditor_uploader.urls')),  # ckeditor related

    # web api
    path('api/auth/', include('rest_framework.urls')),
    path('api/v1/', include([
        path('celeb/', include('celebs.api.urls', namespace='celebs')),
        path('movie/', include('movies.api.urls', namespace='movies')),
        path('account/', include('users.api.urls'))
    ])),

    # data with HTML, no web api (no json data)
    path('', include([
        path('celeb/', include('celebs.urls_html')),
        path('movie/', include('movies.urls_html')),
        path(
            'search/', Search.as_view(template_name=html_dir + 'search.html'),
            name='search'),
        path(
            '', Home.as_view(template_name=html_dir + 'index.html'),
            name='index')
    ])),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns \
      + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
      + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
    # TODO: DRF (json data), vue and jquery consumes web api
    # web api
    path('api/v1/', include([
        path('', include('celebs.api.urls')),
        path('', include('movies.api.urls')),
    ])),

    # TODO: below will web api consuming web pages
    # from DRF (json data)
    path('vue/', include([
        path('celeb/', include('celebs.urls_vue')),
        path('movie/', include('movies.urls_vue')),
    ])),
    # from DRF (json data)
    path('jq/', include([
        path('celeb/', include('celebs.urls_html')),  # TODO: change url file
        path('movie/', include('movies.urls_html')),
    ])),
"""
