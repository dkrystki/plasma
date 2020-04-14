from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"

    image = serializers.ImageField(write_only=True)
    thumbnail = serializers.ImageField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
