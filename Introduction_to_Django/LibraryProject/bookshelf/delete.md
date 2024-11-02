delete.md
book_delete = Book.objects.get(published_year='1949') 
book_delete.delete()
output:  (1, {'bookshelf.Book': 1})