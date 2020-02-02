from rest_framework import serializers

from housing.models import Room, Unit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()

    class Meta:
        model = Room
        fields = "__all__"
