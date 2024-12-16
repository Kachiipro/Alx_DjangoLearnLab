from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from . import views
from .views import FeedView

# Create a router and register viewsets
router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

# URL patterns
urlpatterns = [ path('feed/', FeedView.as_view(), name='feed'),] + router.urls
