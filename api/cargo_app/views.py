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
from api.cargo_app import serializers




class TrackCodeList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.TrackCodeSerializer
    queryset = TrackCode.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['track_code']


class TrackCodeCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.TrackCodeSerializer
    queryset = TrackCode.objects.all()


class TrackCodeGet(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.TrackCodeSerializer
    queryset = models.TrackCode.objects.all()
    lookup_field = 'id'


class TrackCodeUpdate(generics.UpdateAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.TrackCodeSerializer
    queryset = models.TrackCode.objects.all()
    lookup_field = 'id'


class TrackCodeDelete(generics.DestroyAPIView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.TrackCodeSerializer
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


class GroupCreateApiView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupCreateSerializer



class GroupTrackCodeDelete(APIView):

    def delete(self, request, *args, **kwargs):
        ids = request.data.get('ids', [])

        # Проверяем, что ids - это список
        if not isinstance(ids, list):
            return Response({'error': 'Неверный формат данных. Ожидается список идентификаторов.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Удаляем объекты, соответствующие идентификаторам
        for id in ids:
            try:
                obj = TrackCode.objects.get(id=id)
                obj.delete()
            except TrackCode.DoesNotExist:
                # Возвращаем ошибку, если объект не найден
                return Response({'error': f'Объект с идентификатором {id} не найден.'},
                                status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Объекты успешно удалены.'}, status=status.HTTP_200_OK)


class GroupListApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = serializers.GroupListSerializer


class GroupUpdateApiView(generics.UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        data = request.data
        if not isinstance(data, list):
            return Response({'error': 'Неверный формат данных. Ожидается список объектов.'},
                            status=status.HTTP_400_BAD_REQUEST)

        updated_objects = []
        for item in data:
            try:
                # Получаем объект по идентификатору
                obj = Group.objects.get(id=item.get('id'))

                # Обновляем объект с помощью сериализатора
                serializer = self.get_serializer(obj, data=item, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    updated_objects.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except Group.DoesNotExist:
                return Response({'error': f'Объект с идентификатором {item.get("id")} не найден.'},
                                status=status.HTTP_404_NOT_FOUND)

        return Response(updated_objects, status=status.HTTP_200_OK)


class GroupGet(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = serializers.GroupGetSerializer
    lookup_field = 'id'


from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import TrackCode, Group
from . import serializers

class BulkMoveTrackCodeView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.TrackCodeSerializer

    def update(self, request, *args, **kwargs):
        track_code_ids = request.data.get('track_code_ids')
        new_group_id = request.data.get('new_group_id')

        # Validate input
        if not track_code_ids:
            return Response({'error': 'No track codes provided'}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(track_code_ids, list) or not all(isinstance(id, int) for id in track_code_ids):
            return Response({'error': 'track_code_ids must be a list of integers'}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(new_group_id, int):
            return Response({'error': 'new_group_id must be an integer'}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve new group
        try:
            new_group = Group.objects.get(id=new_group_id)
        except Group.DoesNotExist:
            return Response({'error': 'New group not found'}, status=status.HTTP_404_NOT_FOUND)

        # Process track codes
        not_found_ids = []
        for track_code_id in track_code_ids:
            try:
                track_code = TrackCode.objects.get(id=track_code_id)
                track_code.group = new_group
                track_code.save()
            except TrackCode.DoesNotExist:
                not_found_ids.append(track_code_id)

        # Construct response
        if not_found_ids:
            return Response({'error': 'Some track codes not found', 'not_found_ids': not_found_ids}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Track codes moved successfully'}, status=status.HTTP_200_OK)
