from django.urls import include, path
from rest_framework import routers

from tenants import views

app_name = "tenants"

router = routers.DefaultRouter()
router.register(r"applications", views.ApplicationViewSet, basename="applications")
router.register(r"people", views.PeopleViewset, basename="people")
router.register(r"tenants", views.TenantsViewset, basename="tenants")
router.register(r"entry-notices", views.EntryNoticeViewset, basename="entry-notices")
router.register(r"addresses", views.AddressesViewset, basename="addresses")
router.register(r"referrers", views.ReferrersViewset, basename="referrers")


urlpatterns = [
    path("", include(router.urls)),
    path(r"applications/<int:pk>/getlease/", views.GetApplicationLease.as_view(), name="application-getlease"),
    path(r"entry-notices/<int:pk>/send/", views.EntryNoticeSend.as_view(), name="entry-notices-send"),
]
