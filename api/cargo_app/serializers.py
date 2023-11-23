from rest_framework import serializers
from .models import Status, TrackCode, GroupTrackCodes

# Serializer for the Status model
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name_status']

# Serializer for the TrackCode model
class TrackCodeSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField()  # Display the string representation of the group

    class Meta:
        model = TrackCode
        fields = ['id', 'track_code_name', 'group', 'created_at', 'updated_at']

# Serializer for the GroupTrackCodes model
class GroupTrackCodesSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)  # Nested serializer for Status
    group_track_code = TrackCodeSerializer(many=True, read_only=True)  # Nested serializer for related track codes

    class Meta:
        model = GroupTrackCodes
        fields = ['id', 'text_trackCode', 'status', 'date_group_created', 'group_track_code', 'track_codes']
        extra_kwargs = {'date_group_created': {'format': '%d.%m.%Y'}}
