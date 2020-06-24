"""default router/urlpatterns"""
from django.urls import include, path

from rest_framework import routers

from .views import GenreViewSet, MovieViewSet, PgRatingViewsSet

router = routers.DefaultRouter()
router.register('genre', GenreViewSet)
router.register('pg-rating', PgRatingViewsSet)
router.register('', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
