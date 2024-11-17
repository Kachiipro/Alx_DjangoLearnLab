from bookshelf.models import Book
get_book = Book.objects.get(title='1984') 
get_book.title = 'Nineteen Eighty-Four'
get_book.save()

get_book = Book.objects.get(published_year='1949') 
print(f"Title: {get_book.title},Author: {get_book.author},published Year: {get_book.published_year}")
output:  Title: Nineteen Eighty-Four,Author: George Orwell,published Year: 1949