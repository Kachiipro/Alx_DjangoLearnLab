from bookshelf.models import Book
book= Book.objects.get(published_year='1949') 
book.delete()
output:  (1, {'bookshelf.Book': 1})