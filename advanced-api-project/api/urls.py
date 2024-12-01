from django.urls import path
from .views import CustomBookCreateView,CustomBookDetailView,CustomBookListView,CustomBookDeleteView,CustomBookUpdateView

urlpatterns = [
    path('api/', CustomBookListView.as_view(), name='book-list'),
    path('api/<int:pk>/', CustomBookDetailView.as_view(), name='book-detail'),
    path('api/create/', CustomBookCreateView.as_view(), name='book-create'),
    path('api/<int:pk>/update/', CustomBookUpdateView.as_view(), name='book-update'),
    path('api/<int:pk>/delete/', CustomBookDeleteView.as_view(), name='book-delete'),
]