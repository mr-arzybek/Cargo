from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from api.cargo_app import serializers
from rest_framework.views import APIView
from api.cargo_app import models
from api.cargo_app.models import TrackCode, Status, Group
from api.cargo_app.serializers import TrackCodeSerializer, GroupSerializer

from .filters import TrackCodeFilter


class TrackCodeList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TrackCodeSerializer
    queryset = TrackCode.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = TrackCodeFilter
    search_fields = ['track_code']


class TrackCodeCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TrackCodeSerializer
    queryset = TrackCode.objects.all()


class TrackCodeGet(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TrackCodeSerializer
    queryset = models.TrackCode.objects.all()
    lookup_field = 'id'


class TrackCodeUpdate(generics.UpdateAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TrackCodeSerializer
    queryset = models.TrackCode.objects.all()
    lookup_field = 'id'


class TrackCodeDelete(generics.DestroyAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TrackCodeSerializer
    queryset = models.TrackCode.objects.all()
    lookup_field = 'id'


class StatusList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Status.objects.all()
    serializer_class = serializers.StatusSerializer


class StatusDelete(generics.DestroyAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Status.objects.all()
    serializer_class = serializers.StatusSerializer
    lookup_field = 'id'


class CheckTrackCodeView(APIView):
    def post(self, request):
        track_code = request.data.get('track_code', None)

        if track_code is None:
            return Response({'error': 'Пожалуйста, предоставьте код'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            track_code = TrackCode.objects.get(track_code=track_code)
            status_tr = str(track_code.status.name_status)
            date_tr = str(track_code.date)
            return Response({'status': status_tr, 'date': date_tr}, status=HTTP_200_OK)
        except TrackCode.DoesNotExist:
            return Response({'error': 'Код не найден'}, status=HTTP_404_NOT_FOUND)


# class GroupTrackCodeApiView(generics.ListCreateAPIView , generics.RetrieveAPIView , generics.DestroyAPIView):
#     permission_classes = [permissions.IsAdminUser]
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class GroupTrackCodeAddView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupTrackCodeDeleteApiView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupTrackCodePutApiView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'id'


class GroupTrackCodeGetApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'id'
