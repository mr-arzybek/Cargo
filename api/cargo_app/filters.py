import django_filters
from .models import TrackCode


class TrackCodeFilter(django_filters.FilterSet):
    class Meta:
        model = TrackCode
        fields = ['track_code_name']
