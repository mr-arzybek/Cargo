from rest_framework import serializers

from api.cargo_app.models import Status, TrackCode


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TrackCodeSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()


    class Meta:
        model = TrackCode
        fields = '__all__'

    def get_status(self, obj):
        return obj.status.name_status
