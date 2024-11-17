from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

def create_groups_and_permissions():
    # Create groups
    viewers_group, created = Group.objects.get_or_create(name='Viewers')
    editors_group, created = Group.objects.get_or_create(name='Editors')
    admins_group, created = Group.objects.get_or_create(name='Admins')

    
    content_type = ContentType.objects.get_for_model(Book)
    can_view = Permission.objects.get(codename='can_view', content_type=content_type)
    can_create = Permission.objects.get(codename='can_create', content_type=content_type)
    can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
    can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

    
    viewers_group.permissions.add(can_view)

    editors_group.permissions.add(can_view, can_create, can_edit)

    admins_group.permissions.add(can_view, can_create, can_edit, can_delete)

    print("Groups and permissions have been created and assigned.")





@permissionrequired ('Bookshelf.can_add', raise exceptions= true)
def Bookshelf_detail(request, pk):
    Bookshelf = get_object_or_404(Bookshelf, pk=pk)
    return render(request, 'Bookshelf_detail')
@permission_required( 'Bookshelf.can_create', raise_exception=True)
def create_Bookshelf(request):
    if request.method == 'POST':
      title = request.POST.get ('title')
      content = request.POST.get ('content')
      Bookshelf = Bookshelf.objects.create(title=title, content=content)
      return redirect( 'Bookshelf_details')
@permission_required( 'Bookshelf can_edit', raise_exception=True)
def edit_Bookshelf (request):
    if request.method == 'POST':
     title = request. POST.get( 'title')
     content = request. POST. get ('content' )
     Bookshelf = Bookshelf.objects.add (title=title, content=content)
    return redirect( 'Bookshelf_details')


def search_books(request):
    form = ExampLeForm (request, GET)
    if form.is_valid():
      query = form. cleaned_data ['query']
      books = Book.objects.filter(title__icontains=query)
      return render (request, 'bookshelf/book_list.html', {'form': form, 'books': books})