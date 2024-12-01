from django.db import models

# Create your models here.
class Author(models.Model): # author model 
    name = models.CharField(max_length=200)
    
class Book(models.Model): # book model 
    title =models.CharField(max_length=200)
    publication_year=models.IntegerField
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name= 'book') # creating one to many relatiomship with author model 



