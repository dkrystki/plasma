from rest_framework import generics

from tenants.models import Application
from tenants.serializers import ApplicationSerializer

from loguru import logger


class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def post(self, request, *args, **kwargs):
        logger.info("Creating application.")
        return self.create(request, *args, **kwargs)
