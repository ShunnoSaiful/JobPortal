from django.conf import settings
from django.db import models


# MVC MODEL VIEW CONTROLLER


def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    EmployeeModel = instance.__class__
    # new_id = PostModel.objects.order_by("instance.id").last().id + 1

    return "%s" %(filename)

class Portfulio(models.Model):
	name    = models.CharField(max_length=120)
	details = models.TextField(null=True, blank=True)
	link    = models.URLField(max_length=200, null=True, blank=True)
	file    = models.FileField(upload_to=upload_location, null=True, blank=True)


class Address(models.Model):
	city      = models.TextField()
	address   = models.TextField()
	post_code = models.IntegerField(null=True, blank=True)


class SocialLink(models.Model):
	github        = models.URLField(max_length=200, null=True, blank=True)
	stackoverflow = models.URLField(max_length=200, null=True, blank=True)
	linkedin      = models.URLField(max_length=200, null=True, blank=True)
	facebook      = models.URLField(max_length=200, null=True, blank=True)

class Employee(models.Model):
    user               = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    emp_first_name     = models.CharField(max_length=120)
    emp_last_name      = models.CharField(max_length=120)
    emp_username       = models.CharField(max_length=120)
    emp_position_title = models.CharField(max_length=120, null=True, blank=True)
    emp_profile_image  = models.ImageField(upload_to=upload_location, null=True, blank=True)
    emp_info           = models.TextField(null=True, blank=True)
    emp_email          = models.EmailField()
    emp_country        = models.CharField(max_length=20)
    emp_address        = models.ForeignKey(Address, on_delete=models.CASCADE)
    emp_skills         = models.TextField()
    emp_resume         = models.FileField(upload_to=upload_location, null=True, blank=True)
    emp_portfulio      = models.ForeignKey(Portfulio, on_delete=models.CASCADE, null=True, blank=True)
    emp_social_link    = models.ForeignKey(SocialLink, on_delete=models.CASCADE, null=True, blank=True)
    emp_ratting        = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True)
    emp_review         = models.CharField(max_length=150, null=True, blank=True)
    emp_password       = models.CharField(max_length=30)
    profile_created    = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.emp_username


    class Meta:
        ordering = ["-profile_created"]












