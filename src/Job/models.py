from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from Company.models import Company
# MVC MODEL VIEW CONTROLLER

EMPLOYMENT_STATUS_CHOICES = (
        ('fulltime', 'Full Time'),
        ('parttime', 'Part Time'),
        ('remote', 'Remote')
    )




class Job(models.Model):
    company               = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    position              = models.CharField(max_length=120)
    vacancy               = models.IntegerField(null=True, blank=True)
    job_context 	      = models.CharField(max_length=500, null=True, blank=True)
    job_responsibility    = models.CharField(max_length=500, null=True, blank=True)
    employment_status     = models.CharField(max_length=1, choices=EMPLOYMENT_STATUS_CHOICES, null=True, blank=True)
    educational_req       = models.CharField(max_length=500, null=True, blank=True)
    experience_req        = models.CharField(max_length=500, null=True, blank=True)
    additional_req        = models.CharField(max_length=500, null=True, blank=True)
    job_location          = models.CharField(max_length=500, null=True, blank=True)
    salaray               = models.IntegerField(null=True, blank=True)
    compensation          = models.CharField(max_length=500, null=True, blank=True)
    application_deadline  = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    application_procedure = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=True)
    publish_on     	 	  = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return str(self.position)


    class Meta:
        ordering = ["-publish_on"]