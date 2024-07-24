from rest_framework.routers import DefaultRouter
from django.urls import path, include

from chat.views import ChatViewSet

router = DefaultRouter()
router.register("chat", ChatViewSet, basename="chat"),


urlpatterns = [path("", include(router.urls))]

app_name = "chat"
