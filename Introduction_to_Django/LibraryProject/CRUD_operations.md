create.md
new_book = Book(title='1984',author='George Orwell',published_year='1949')  
new_book.save()

retrieve.md
get_book = Book.objects.get(title='1984')      
print(f"Title: {get_book.title},Author: {get_book.author},published Year: {get_book.published_year}")

output--  Title: 1984,Author: George Orwell,publishe Year: 1949

Update.md 
get_book = Book.objects.get(title='1984') 
get_book.title = 'Nineteen Eighty-Four'
get_book.save()

get_book = Book.objects.get(published_year='1949') 
print(f"Title: {get_book.title},Author: {get_book.author},published Year: {get_book.published_year}")
output:  Title: Nineteen Eighty-Four,Author: George Orwell,published Year: 1949


delete.md
book_delete = Book.objects.get(published_year='1949') 
book_delete.delete()
(1, {'bookshelf.Book': 1})

