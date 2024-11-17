retrieve.md
get_book = Book.objects.get(title='1984')      
print(f"Title: {get_book.title},Author: {get_book.author},published Year: {get_book.published_year}")

output--  Title: 1984,Author: George Orwell,publishe Year: 1949