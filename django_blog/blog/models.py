from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User  = get_user_model()
class post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=200)
    published_date= models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'posts', default=None , null=True)