import django_filters
from .models import TrackCode, Group


# class TrackCodeFilter(django_filters.FilterSet):
#     class Meta:
#         model = TrackCode
#         fields = ['status__id']

class GroupStatusFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = ['status__name_status']



