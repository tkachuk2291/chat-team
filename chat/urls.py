from rest_framework.routers import DefaultRouter
from django.urls import path, include

from chat.views import ChatViewSet, CategoryViewSet

router = DefaultRouter()
router.register("chat", ChatViewSet, basename="chat"),
router.register("category", CategoryViewSet, basename="category"),

urlpatterns = [path("", include(router.urls))]

app_name = "chat"
