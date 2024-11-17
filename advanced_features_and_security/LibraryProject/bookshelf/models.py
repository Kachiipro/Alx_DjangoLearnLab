from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year =models.IntegerField(default=0000)


    def __str__(self):
        return f"{self.title} {self.author} {self.published_year}"
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username