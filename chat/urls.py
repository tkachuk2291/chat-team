from rest_framework.routers import DefaultRouter
from django.urls import path, include

from chat.views import UserViewSet

router = DefaultRouter()
router.register("user", UserViewSet, basename="user"),

urlpatterns = [path("", include(router.urls))]

app_name = "films"
