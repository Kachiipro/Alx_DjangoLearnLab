from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FollowViewSet
from .views import UserRegistrationView, UserLoginView


router = DefaultRouter()
router.register('follow', FollowViewSet, basename='follow')



urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
] + router.urls