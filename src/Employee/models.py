from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from .utils import unique_slug_generator


# MVC MODEL VIEW CONTROLLER


def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s.%s" %(instance.user, instance.user, extension)
    EmployeeModel = instance.__class__
    new_id = EmployeeModel.objects.order_by("instance.user").last().id + 1

    return "%s" %(filename)

class Portfulio(models.Model):
    title   = models.CharField(max_length=120)
    details = models.TextField(null=True, blank=True)
    link    = models.URLField(max_length=200, null=True, blank=True)
    file    = models.FileField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return self.title


class Address(models.Model):
    city      = models.TextField()
    address   = models.TextField()
    post_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.city


class SocialLink(models.Model):
    github        = models.URLField(max_length=200, null=True, blank=True)
    stackoverflow = models.URLField(max_length=200, null=True, blank=True)
    linkedin      = models.URLField(max_length=200, null=True, blank=True)
    facebook      = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.github

class Employee(models.Model):
    user               = models.OneToOneField(User, on_delete=models.CASCADE)
    slug               = models.SlugField(unique=True, null=True, blank=True)
    emp_first_name     = models.CharField(max_length=120)
    emp_last_name      = models.CharField(max_length=120)
    emp_position_title = models.CharField(max_length=120, null=True, blank=True)
    emp_overview       = models.TextField(null=True, blank=True)
    emp_experience     = models.TextField(null=True, blank=True)
    emp_education      = models.TextField(null=True, blank=True)
    emp_profile_image  = models.ImageField(upload_to=upload_location, null=True, blank=True)
    emp_info           = models.TextField(null=True, blank=True)
    emp_email          = models.EmailField()
    emp_country        = models.CharField(max_length=20)
    emp_address        = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    emp_skills         = models.TextField()
    # following        = models.ManyToManyField(User, related_name='followers')
    # followers        = models.ManyToManyField(User, related_name='following')
    emp_resume         = models.FileField(upload_to=upload_location, null=True, blank=True)
    emp_portfulio      = models.ForeignKey(Portfulio, on_delete=models.CASCADE, null=True, blank=True)
    emp_social_link    = models.ForeignKey(SocialLink, on_delete=models.CASCADE, null=True, blank=True)
    emp_ratting        = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True)
    emp_review         = models.CharField(max_length=150, null=True, blank=True)
    profile_created    = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return str(self.user)


    class Meta:
        ordering = ["-profile_created"]
        

    
class FollowRequest(models.Model):
    user              = models.ForeignKey(User, on_delete=models.CASCADE,default='0') # user.profile
    followers         = models.ManyToManyField(User, related_name='is_following', blank=True) # user.is_following.all()
    following         = models.ManyToManyField(User, related_name='following', blank=True) # user.following.all()
    activated         = models.BooleanField(default=False)
    timestamp         = models.DateTimeField(auto_now_add=True)
    updated           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


def create_slug(instance, new_slug=None):
    slug = slugify(instance.user)
    if new_slug is not None:
        slug = new_slug
    qs = Employee.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_job_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_job_receiver, sender=Employee)






