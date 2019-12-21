from django.urls import path, include
from rest_framework import routers

from tenants import views

app_name = "tenants"

router = routers.DefaultRouter()
router.register(r'applications', views.CrudApplication, basename="application")


urlpatterns = [
    path('', include(router.urls)),
    path(r'applications/<int:pk>/getlease/', views.GetApplicationLease.as_view(), name="application-getlease"),
]
