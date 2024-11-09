from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year =models.IntegerField(default=0000)


    def __str__(self):
        return f"{self.title} {self.author} {self.published_year}"