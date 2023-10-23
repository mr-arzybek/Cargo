from rest_framework import serializers

from api.cargo_app.models import Status, TrackCode


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        exclude = 'id'.split()


class TrackCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackCode
        fields = '__all__'


class CheckTrackCodeSerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=False)

    class Meta:
        model = TrackCode
        fields = ['name_status', ]