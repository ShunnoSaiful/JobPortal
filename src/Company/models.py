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
    CompanyModel = instance.__class__
    new_id = CompanyModel.objects.order_by("instance.user").last().id + 1

    return "%s" %(filename)


class Address(models.Model):
    city      = models.TextField()
    address   = models.TextField()
    post_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.city



class Company(models.Model):
    user                   = models.OneToOneField(User, on_delete=models.CASCADE)
    slug                   = models.SlugField(unique=True, null=True, blank=True)
    company_name           = models.CharField(max_length=120)
    company_title          = models.CharField(max_length=120, null=True, blank=True)
    company_profile_image  = models.ImageField(upload_to=upload_location, null=True, blank=True)
    company_info           = models.TextField(null=True, blank=True)
    company_email          = models.EmailField()
    company_country        = models.CharField(max_length=20)
    company_address        = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    # following            = models.ManyToManyField(User, related_name='followers')
    # followers            = models.ManyToManyField(User, related_name='following')
    company_web_link       = models.URLField(max_length=200, null=True, blank=True)
    company_ratting        = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True)
    company_review         = models.CharField(max_length=150, null=True, blank=True)
    profile_created        = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_company             = models.BooleanField(default=True)


    def __str__(self):
        return str(self.user)


    class Meta:
        ordering = ["-profile_created"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.user)
    if new_slug is not None:
        slug = new_slug
    qs = Company.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_job_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_job_receiver, sender=Company)

