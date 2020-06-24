"""default router/urlpatterns"""
from django.urls import include, path

from rest_framework import routers

from users.models import Group, User
from .views import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('group', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
