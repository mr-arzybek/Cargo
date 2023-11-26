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
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

class DeleteTrackCodesFromGroup(APIView):

    def post(self, request, *args, **kwargs):
        group_id = request.data.get('group_id')
        track_code_ids = request.data.get('track_code_ids', [])

        # Make sure group_id is provided and valid
        if not group_id:
            return JsonResponse({'error': 'No group ID provided.'}, status=status.HTTP_400_BAD_REQUEST)

        # Make sure track_code_ids is a list of integers
        try:
            track_code_ids = [int(id) for id in track_code_ids]
        except (ValueError, TypeError):
            return JsonResponse({'error': 'track_code_ids must be a list of integers.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return JsonResponse({'error': 'Group not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Filter track codes that exist and are part of the group
        existing_track_codes = TrackCode.objects.filter(id__in=track_code_ids, group=group)

        # Delete the track codes
        deleted_count, _ = existing_track_codes.delete()

        if deleted_count < len(track_code_ids):
            message = f'Some track codes were not found in the specified group and skipped. {deleted_count} track codes deleted from the group.'
        else:
            message = 'All provided track codes in the specified group were successfully deleted.'

        return JsonResponse({'message': message}, status=status.HTTP_200_OK)
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
            track_code_obj = TrackCode.objects.get(track_code=track_code)
            group_status = str(track_code_obj.group.status)
            group_date = str(track_code_obj.group.date)
            return Response({'status': group_status, 'date': group_date}, status=status.HTTP_200_OK)
        except TrackCode.DoesNotExist:
            return Response({'error': 'Код не найден'}, status=status.HTTP_404_NOT_FOUND)


class GroupCreateApiView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupCreateSerializer


class GroupTrackCodeDelete(APIView):
    def delete(self, request, *args, **kwargs):
        track_code_ids = request.data.get('track_code_ids', [])

        # Проверяем, является ли track_code_ids строкой и пытаемся ее десериализовать
        if isinstance(track_code_ids, str):
            try:
                track_code_ids = json.loads(track_code_ids)
            except json.JSONDecodeError:
                return Response({'error': 'Invalid format for track_code_ids'}, status=status.HTTP_400_BAD_REQUEST)

        # Получаем список объектов для удаления
        objects_to_delete = TrackCode.objects.filter(id__in=track_code_ids)
        found_ids = [obj.id for obj in objects_to_delete]
        missing_ids = list(set(track_code_ids) - set(found_ids))

        if missing_ids:
            # Удаляем найденные объекты
            objects_to_delete.delete()
            return Response({
                                'warning': f'Некоторые объекты с идентификаторами {missing_ids} не найдены. Остальные объекты удалены.'},
                            status=status.HTTP_200_OK)

        # Удаляем все найденные объекты, если нет отсутствующих ID
        objects_to_delete.delete()
        return Response({'message': 'Все объекты успешно удалены.'}, status=status.HTTP_200_OK)


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
from .models import Group, TrackCode
from . import serializers
import json


class BulkMoveTrackCodeView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.TrackCodeSerializer

    def update(self, request, *args, **kwargs):
        # Extract and validate the track code IDs and new group ID from the request
        track_code_ids = request.data.get('track_code_ids')
        new_group_id = request.data.get('new_group_id')

        # Check if track_code_ids is a string and try to parse it as JSON
        if isinstance(track_code_ids, str):
            try:
                track_code_ids = json.loads(track_code_ids)
            except json.JSONDecodeError:
                return Response({'error': 'Invalid format for track_code_ids'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the track code IDs
        if not track_code_ids:
            return Response({'error': 'No track codes provided'}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(track_code_ids, list) or not all(isinstance(id, int) for id in track_code_ids):
            return Response({'error': 'track_code_ids must be a list of integers'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the new group ID
        try:
            new_group_id = int(new_group_id)
        except ValueError:
            return Response({'error': 'new_group_id must be an integer'}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve and validate the new group
        try:
            new_group = Group.objects.get(id=new_group_id)
        except Group.DoesNotExist:
            return Response({'error': 'New group not found'}, status=status.HTTP_404_NOT_FOUND)

        # Initialize a list for not found track code IDs
        not_found_ids = []

        # Update each track code's group if it exists
        for track_code_id in track_code_ids:
            try:
                track_code = TrackCode.objects.get(id=track_code_id)
                track_code.group = new_group
                track_code.save()
            except TrackCode.DoesNotExist:
                not_found_ids.append(track_code_id)

        # Add a response for track codes that were not found
        if not_found_ids:
            return Response({'not_found_ids': not_found_ids}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Track codes successfully updated'}, status=status.HTTP_200_OK)
