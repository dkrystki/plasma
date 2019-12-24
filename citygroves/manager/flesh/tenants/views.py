from pathlib import Path

from django.db.models import Prefetch
from django.http import HttpResponse
from rest_framework import generics, mixins, viewsets

from tenants import models
from tenants import serializers

import logging

logger = logging.getLogger(__name__)


class ApplicationViewSet(viewsets.GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin):
    queryset = models.Application.objects.prefetch_related(Prefetch('referrers',
                                                                    queryset=models.Referrer.objects.order_by('id')))
    serializer_class = serializers.ApplicationSerializer


class PeopleViewset(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class ReferrersViewset(viewsets.GenericViewSet,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin):
    queryset = models.Referrer.objects.all()
    serializer_class = serializers.ReferrerSerializer


class AddressesViewset(viewsets.GenericViewSet,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


class GetApplicationLease(generics.RetrieveAPIView):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer

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
