from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
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
    user               = models.ForeignKey(User, on_delete=models.CASCADE)
    emp_first_name     = models.CharField(max_length=120)
    emp_last_name      = models.CharField(max_length=120)
    emp_position_title = models.CharField(max_length=120, null=True, blank=True)
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

from django import forms

# def post_save_user_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         profile, is_created = Employee.objects.get_or_create(emp_username=instance, emp_email=instance.email)

# post_save.connect(post_save_user_receiver, sender=User) 








