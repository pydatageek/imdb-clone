"""default router/urlpatterns"""
from django.urls import include, path

from rest_framework import routers

from .views import CelebrityApiViewSet, DutyApiViewSet

app_name = 'celebs'

router = routers.DefaultRouter()
router.register('duty', DutyApiViewSet)
router.register('', CelebrityApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
