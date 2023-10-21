import django_filters
from .models import TrackCode


class TrackCodeFilter(django_filters.FilterSet):
    class Meta:
        model = TrackCode
        fields = ['status__id']
