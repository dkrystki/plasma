from pathlib import Path
from typing import List

from django.db.models import Prefetch
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, viewsets
from rest_framework.request import Request

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


class GetApplicationLease(generics.RetrieveAPIView):
    queryset = models.Application.objects.all()

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


class PeopleViewset(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class TenantsViewset(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin):
    queryset = models.Tenant.objects.all()
    serializer_class = serializers.TenantSerializer


class EntryNoticeViewset(viewsets.GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin):
    queryset = models.EntryNotice.objects.all()
    serializer_class = serializers.EntryNoticeSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get_queryset(self):
        if "id" in self.request.query_params:
            return self.queryset.filter(pk__in=self.get_ids())
        else:
            return self.queryset

    def get_ids(self) -> List[int]:
        return self.request.query_params.get('id').split(",")

    def list(self, request, *args, **kwargs):
        if "pdf" in self.request.query_params:
            files: List[Path] = []
            for en in self.get_queryset():
                path = Path(f"/tmp/{str(en)}.pdf")
                files.append(path)
                en.create_pdf(path)
            logger.info(f"Preparing entry notice documents for {str(self.get_ids())}")
        else:
            return super().list(self)


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
