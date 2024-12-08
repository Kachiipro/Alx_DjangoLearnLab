from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from taggit.managers import TaggableManager
from taggit.models import TagBase
from django.utils.text import slugify
from taggit.models import TagBase, GenericTaggedItemBase
from django.db import models
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date= models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'posts', default=None , null=True)
    tags = TaggableManager()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return self.user.username
    


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
        
        

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
    
class CustomTag(TagBase):
    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
class CustomTaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(
        CustomTag,
        on_delete=models.CASCADE,
        related_name="tagged_items"
    )