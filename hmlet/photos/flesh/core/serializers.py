from datetime import datetime

from django.contrib.auth.models import User
from pytz import UTC
from rest_framework import serializers

from core.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"

    image = serializers.ImageField(write_only=True)
    thumbnail = serializers.ImageField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault(),
                                              write_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    publish_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        obj = Photo.objects.create(**validated_data,
                                   publish_date=datetime.now(tz=UTC))
        return obj

    def get_username(self, obj):
        return obj.user.username
