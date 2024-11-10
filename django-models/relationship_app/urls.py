from django.urls import path
from .views import list_books,LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
urlpatterns= [
    path('', views= list_books, name = 'book_list'),
    path('', views= LibraryDetailView, name = 'book_list'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
