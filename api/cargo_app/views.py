from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from api.cargo_app import serializers
from api.cargo_app import models
from api.cargo_app.models import TrackCode, Status
from api.cargo_app.serializers import TrackCodeSerializer


class TrackCodeList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TrackCodeSerializer
    queryset = models.TrackCode.objects.all()


class TrackCodeCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TrackCodeSerializer
    queryset = models.TrackCode.objects.all()


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


class StatusUpdate(generics.UpdateAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.StatusSerializer
    queryset = models.Status.objects.all()
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
    def get(self, request):
        code = request.query_params.get('code', None)

        if code is None:
            return Response({'error': 'Пожалуйста, предоставьте код'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            track_code = TrackCode.objects.get(code=code)
            status_tr = str(track_code.status)
            return Response({'status': status_tr}, status=status.HTTP_200_OK)
        except TrackCode.DoesNotExist:
            return Response({'error': 'Код не найден'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        code = request.data.get('code', None)

        if code is None:
            return Response({'error': 'Пожалуйста, предоставьте код'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            track_code = TrackCode.objects.get(code=code)
            status_tr = str(track_code.status)  # Преобразование статуса в строку
            return Response({'status': status_tr}, status=HTTP_200_OK)
        except TrackCode.DoesNotExist:
            return Response({'error': 'Код не найден'}, status=HTTP_404_NOT_FOUND)
