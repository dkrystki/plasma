from django.urls import path
from tenants import views

app_name = "tenants"

urlpatterns = [
    path('application/create/', views.CreateApplication.as_view(), name="application-create"),
    path(r'application/<int:pk>/getlease/', views.GetApplicationLease.as_view(), name="application-getlease"),
]
