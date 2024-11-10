from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs/')
    content = RichTextUploadingField()  # for rich text editing
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts', blank=True) 

    def _str_(self):
        return self.title


@receiver(pre_delete, sender=BlogPost)
def delete_image(sender, instance, **kwargs):
    """Supprimer l'image associée à l'instance avant la suppression."""
    if hasattr(instance, 'image') and instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)