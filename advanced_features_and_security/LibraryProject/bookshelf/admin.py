from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class BookAdmin(admin.ModelAdmin):

    list_filter= ('author', 'published_year')
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'date_of_birth')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)
    admin.site.register(CustomUser, CustomUserAdmin)
    
admin.site.register(Book, BookAdmin)