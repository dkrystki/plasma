from django.urls import path, include
from rest_framework import routers

from tenants import views

app_name = "tenants"

router = routers.DefaultRouter()
router.register(r'applications', views.ApplicationViewSet, basename="application")
router.register(r'people', views.PeopleViewset, basename="people")
router.register(r'tenants', views.TenantsViewset, basename="tenants")
router.register(r'addresses', views.AddressesViewset, basename="addresses")
router.register(r'referrers', views.ReferrersViewset, basename="referrers")


urlpatterns = [
    path('', include(router.urls)),
    path(r'applications/<int:pk>/getlease/', views.GetApplicationLease.as_view(), name="application-getlease"),
]
