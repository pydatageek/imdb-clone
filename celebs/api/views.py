"""simple base viewsets"""
from rest_framework import viewsets

from celebs.models import Celebrity, Duty
from .serializers import CelebritySerializer, DutySerializer


class CelebrityViewSet(viewsets.ModelViewSet):
    queryset = Celebrity.objects.prefetch_related('duties')
    serializer_class = CelebritySerializer


class DutyViewSet(viewsets.ModelViewSet):
    queryset = Duty.objects.all()
    serializer_class = DutySerializer
