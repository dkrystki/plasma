from pathlib import Path
from typing import List
from zipfile import ZipFile

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

    def retrieve(self, request, *args, **kwargs):
        if [param for param in self.request.query_params if "pdf" in param]:
            obj: models.EntryNotice = self.get_object()
            logger.info(f"Preparing entry notice pdfdocuments for ({str(obj)})")
            files: List[Path] = []
            path = Path(f"/tmp/{str(obj)}.pdf")
            obj.create_pdf(path)

            response = HttpResponse(open(str(path), "rb") , content_type='application/pdf')

            response['Content-Disposition'] = f'attachment; filename={path.stem}'

            logger.info(f"Sending the pdf file ({path.stem}) back to the client agent.")
            return response
        else:
            return super().retrieve(self)


class EntryNoticeSend(generics.GenericAPIView):
    queryset = models.EntryNotice.objects.all()

    def post(self, request, *args, **kwargs):
        obj: models.EntryNotice = self.get_object()
        logger.info(f"Sending entry notice to users email ({str(obj)})")
        obj.send()

        return HttpResponse(200)


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
