from rest_framework import serializers

from api.cargo_app.models import Status, TrackCode, GroupTrackCodes


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class StatusForTrackCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = 'name_status'


class TrackCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackCode
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    track_codes = TrackCodeSerializer(many=True)
    statuses = StatusSerializer()

    class Meta:
        model = GroupTrackCodes
        fields = '__all__'
