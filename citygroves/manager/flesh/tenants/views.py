from rest_framework import generics

from tenants.models import Application
from tenants.serializers import ApplicationSerializer


class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
