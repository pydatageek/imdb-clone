"""default router/urlpatterns"""
from django.urls import include, path

from rest_framework import routers

from .views import GenreApiViewSet, MovieApiViewSet, PgRatingApiViewSet

app_name = 'movies'

router = routers.DefaultRouter()
router.register('genre', GenreApiViewSet)
router.register('pg-rating', PgRatingApiViewSet)
router.register('', MovieApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
