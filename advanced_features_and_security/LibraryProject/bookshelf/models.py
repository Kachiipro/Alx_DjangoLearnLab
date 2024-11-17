from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year =models.IntegerField(default=0000)


    def __str__(self):
        return f"{self.title} {self.author} {self.published_year}"
    
class CustomUserManager(AbstractBaseUser):
    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, date_of_birth=None, profile_photo=None):
        user = self.create_user(username, email, password, date_of_birth, profile_photo)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
  
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username 

