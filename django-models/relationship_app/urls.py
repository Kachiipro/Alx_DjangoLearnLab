from django.urls import path
from .views import list_books,LibraryDetailView
urlpatterns= [
    path('', views= list_books, name = 'book_list'),
    path('', views= LibraryDetailView, name = 'book_list')
]
