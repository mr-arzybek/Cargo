from rest_framework import serializers

from api.cargo_app.models import Status, TrackCode, Group






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
    track_codes = TrackCodeSerializer(many=True, read_only=True)
    status = StatusSerializer()

    class Meta:
        model = Group
        fields = '__all__'


class GroupListSerializer(serializers.ModelSerializer):
    track_codes = TrackCodeSerializer(many=True)
    track_code = TrackCodeSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = '__all__'




class GroupGetSerializer(serializers.ModelSerializer):
    track_codes = TrackCodeSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = '__all__'


class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group