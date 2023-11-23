
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView

from api.cargo_app import serializers
from api.cargo_app.filters import TrackCodeFilter
from api.cargo_app.models import TrackCode, GroupTrackCodes, Status
from api.cargo_app.serializers import TrackCodeSerializer, GroupTrackCodesSerializer


class TrackCodeList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TrackCodeSerializer
    queryset = TrackCode.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = TrackCodeFilter
    search_fields = ['track_code_name']

class TrackCodeCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TrackCodeSerializer
    queryset = TrackCode.objects.all()

class TrackCodeGet(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TrackCodeSerializer
    queryset = TrackCode.objects.all()
    lookup_field = 'id'

class TrackCodeUpdate(generics.UpdateAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TrackCodeSerializer
    queryset = TrackCode.objects.all()
    lookup_field = 'id'

class TrackCodeDelete(generics.DestroyAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TrackCodeSerializer
    queryset = TrackCode.objects.all()
    lookup_field = 'id'


class GroupTrackCodeAddView(generics.ListCreateAPIView):
    queryset = GroupTrackCodes.objects.all()
    serializer_class = GroupTrackCodesSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        group = serializer.save()
        status_id = self.request.data.get('status_id')
        if status_id:
            status = Status.objects.get(id=status_id)
            group.statuses = status
        track_codes_ids = self.request.data.get('track_codes', [])
        for tc_id in track_codes_ids:
            track_code = TrackCode.objects.get(id=tc_id)
            group.track_codes.add(track_code)
        group.save()

class GroupTrackCodeDeleteApiView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = TrackCode.objects.all()
    serializer_class = GroupTrackCodesSerializer
    lookup_field = 'id'

class GroupTrackCodeUpdateApiView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = GroupTrackCodes.objects.all()
    serializer_class = GroupTrackCodesSerializer
    lookup_field = 'id'


class GroupTrackCodeGetApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = GroupTrackCodes.objects.all()
    serializer_class = GroupTrackCodesSerializer
class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [permissions.IsAdminUser]

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

class StatusList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Status.objects.all()
    serializer_class = serializers.StatusSerializer


class StatusDelete(generics.DestroyAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Status.objects.all()
    serializer_class = serializers.StatusSerializer
    lookup_field = 'id'