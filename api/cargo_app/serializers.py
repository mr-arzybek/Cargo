from rest_framework import serializers

from api.cargo_app.models import Status, TrackCode


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TrackCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackCode
        fields = '__all__'


class CheckTrackCodeSerializer(serializers.ModelSerializer):
    code = StatusSerializer(many=False)

    class Meta:
        model = TrackCode
        fields = ['code', 'status']
