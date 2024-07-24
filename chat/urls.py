from rest_framework.routers import DefaultRouter
from django.urls import path, include

from chat.views import ChatViewSet, CategoryViewSet, MessageViewSet

router = DefaultRouter()
router.register("chat", ChatViewSet, basename="chat"),
router.register("category", CategoryViewSet, basename="category"),
router.register("message", MessageViewSet, basename="message"),

urlpatterns = [path("", include(router.urls))]

app_name = "chat"
