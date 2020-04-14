import logging

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from core import serializers
from core.models import Photo

from rest_framework import filters

logger = logging.getLogger(__name__)


class PhotosViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = Photo.objects.all()
    serializer_class = serializers.PhotoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = (IsAuthenticated,)

    search_fields = ['=user__username']
    ordering_fields = ['publish_date']


