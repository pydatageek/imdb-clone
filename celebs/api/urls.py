"""default router/urlpatterns"""
from django.urls import include, path

from rest_framework import routers

from .views import CelebrityViewSet, DutyViewSet

router = routers.DefaultRouter()
router.register('duty', DutyViewSet)
router.register('', CelebrityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
