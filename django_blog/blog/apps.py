from django.apps import AppConfig
from django.utils.module_loading import import_string
from taggit.models import Tag

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    
    def ready(self):
        # Swap out the default Tag model with the CustomTag
        tag_model = import_string("blog.models.CustomTag")
        Tag._meta.get_field("tag").remote_field.model = tag_model