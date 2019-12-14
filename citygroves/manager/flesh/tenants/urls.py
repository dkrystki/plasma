from django.urls import path
from tenants import views

app_name = "tenants"

urlpatterns = [
    path('application/create', views.ApplicationCreate.as_view(), name="application-create"),
]
