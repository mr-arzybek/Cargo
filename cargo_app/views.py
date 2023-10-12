from rest_framework import generics
from rest_framework import permissions

from cargo_app import models
from cargo_app.serializers import TrackCodeSerializer


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
