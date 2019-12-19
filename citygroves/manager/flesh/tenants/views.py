from pathlib import Path

from django.http import HttpResponse
from rest_framework import generics

from tenants.models import Application
from tenants.serializers import ApplicationSerializer

import logging


logger = logging.getLogger(__name__)


class CreateApplication(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def post(self, request, *args, **kwargs):
        logger.info("Creating application.")
        return self.create(request, *args, **kwargs)


class GetApplicationLease(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get(self, request, *args, **kwargs):
        application = self.get_object()
        logger.info(f"Preparing a lease document for {str(application.person)}")

        file_path = Path("/tmp/lease.pdf")
        application.save_lease_pdf(file_path)
        response = HttpResponse(open(str(file_path), "rb"), content_type='application/pdf')

        pdf_name = f"{str(application)}_Lease.pdf"
        response['Content-Disposition'] = f'attachment; filename={pdf_name}'

        logger.info(f"Sending the pdf file ({pdf_name}) back to the client agent.")
        return response
