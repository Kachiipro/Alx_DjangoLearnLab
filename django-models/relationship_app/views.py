from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = Library.objects.all()
        
class register(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

def is_admin(user):
    try:
        return user.userprofile.role == 'Admin'
    except UserProfile.DoesNotExist:
        return False

@user_passes_test(is_admin)  
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_view.html')




def is_librarian(user):
    try:
        return user.userprofile.role == 'Librarian'
    except UserProfile.DoesNotExist:
        return False

@user_passes_test(is_librarian)  
def librarian_dashboard(request):
    return render(request, 'relationship_app/librarian_view.html')


def is_member(user):
    try:
        return user.userprofile.role == 'Member'
    except UserProfile.DoesNotExist:
        return False

@user_passes_test(is_member) 
def member_dashboard(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def add_book_view(request):
    return render(request, 'can_change_book.html')
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def add_book_view(request):
    return render(request, 'can_delete_book.html')