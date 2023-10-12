from rest_framework import serializers

from cargo_app.models import Status, TrackCode


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['name_status', 'description_status', 'track_code']


class TrackCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackCode
        fields = '__all__'
