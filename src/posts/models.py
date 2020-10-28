from __future__ import unicode_literals

from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from markdown_deux import markdown
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from .utils import unique_slug_generator
# Create your models here.

class PostQuerySet(models.query.QuerySet):
    def not_draft(self):
        return self.filter(draft=False)
    
    def published(self):
        return self.filter(publish__lte=timezone.now()).not_draft()

class PostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return PostQuerySet(self.model, using=self._db)
            
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return self.get_queryset().published()



def upload_location(instance, filename):
    return '/'.join(['content', instance.user.username, filename])


class Post(models.Model):
    user         = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    content      = models.TextField(null=True, blank=True)
    slug         = models.SlugField(unique=True)
    image        = models.ImageField(upload_to=upload_location, 
                    null=True, 
                    blank=True, 
                    width_field="width_field", 
                    height_field="height_field")
    video        = models.FileField(upload_to=upload_location, 
                    null=True, 
                    blank=True)
    height_field = models.IntegerField(null=True, blank=True)
    width_field  = models.IntegerField(null=True, blank=True)
    draft        = models.BooleanField(default=False)
    publish      = models.DateField(auto_now=False, auto_now_add=False)
    updated      = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp    = models.DateTimeField(auto_now=False, auto_now_add=True)


    objects = PostManager()

    def __str__(self):
        return self.content


    class Meta:
        ordering = ["-timestamp", "-updated"]
       

    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)
