from django.shortcuts import render
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

@permission_required
def article_view(request):

      book_list = ('app_name.can_edit', raise_exception=True)