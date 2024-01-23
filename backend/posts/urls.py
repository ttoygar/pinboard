from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet, ThreadViewSet

router = DefaultRouter()
router.register(r'threads', ThreadViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
path('', include(router.urls)),
]