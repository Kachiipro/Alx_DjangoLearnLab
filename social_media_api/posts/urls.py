from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

# URL patterns
urlpatterns = [] + router.urls
