from django.urls import include, path
from rest_framework import routers

from core import views

app_name = "core"

router = routers.DefaultRouter()
router.register(r"photos", views.PhotosViewSet, basename="photos")


urlpatterns = [
    path("", include(router.urls)),
]
