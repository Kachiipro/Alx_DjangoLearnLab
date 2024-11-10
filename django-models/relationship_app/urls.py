from django.urls import path
from .views import list_books,LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns= [
    path('', views= list_books, name = 'book_list'),
    path('', views= LibraryDetailView, name = 'book_list'),
    path("signup/", views.register, name="templates/registration/signup"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('librarian/', views.librarian_dashboard, name='librarian_dashboard'),
    path('member/', views.member_dashboard, name='member_dashboard'),
    path('add_book/', views.add_book_view, name='add_book'),
    path('edit_book/<int:book_id>/', views.change_book_view, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book_view, name='delete_book'),
]
