"""simple base viewsets"""
from django.db.models import Prefetch

from rest_framework import viewsets

from celebs.models import Celebrity, Duty
from .serializers import CelebritySerializer, DutySerializer


class CelebrityApiViewSet(viewsets.ModelViewSet):
    queryset = Celebrity.objects.prefetch_related(
        Prefetch('duties', Duty.objects.only('id'))
    )
    serializer_class = CelebritySerializer
    lookup_field = 'slug'
    # permission_classes =


class DutyApiViewSet(viewsets.ModelViewSet):
    queryset = Duty.objects.prefetch_related(
        Prefetch('celebs', Celebrity.objects.only('id'))
    )
    serializer_class = DutySerializer
    lookup_field = 'slug'
    # permission_classes =
