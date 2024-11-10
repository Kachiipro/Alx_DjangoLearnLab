from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):

    list_filter= ('author', 'published_year')
    search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)