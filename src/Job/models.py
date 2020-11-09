from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from Company.models import Company
from django.utils import timezone
from django.db.models.signals import pre_save
from django.utils.text import slugify
from .utils import unique_slug_generator
from markdown_deux import markdown
from django.utils.safestring import mark_safe


# MVC MODEL VIEW CONTROLLER


class JobPostQuerySet(models.query.QuerySet):
    def not_draft(self):
        return self.filter(draft=True)
    
    def deadlined(self):
        return self.filter(application_deadline__lte=timezone.now()).not_draft()

class JobPostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return JobPostQuerySet(self.model, using=self._db)
            
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return self.get_queryset().deadlined()



EMPLOYMENT_STATUS_CHOICES = (
        ('f', 'Full Time'),
        ('p', 'Part Time'),
        ('r', 'Remote')
    )




class Job(models.Model):
    company               = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    position              = models.CharField(max_length=120)
    vacancy               = models.IntegerField(null=True, blank=True)
    job_context 	      = models.CharField(max_length=1500, null=True, blank=True)
    job_responsibility    = models.CharField(max_length=1500, null=True, blank=True)
    employment_status     = models.CharField(max_length=1, choices=EMPLOYMENT_STATUS_CHOICES, null=True, blank=True)
    educational_req       = models.CharField(max_length=1500, null=True, blank=True)
    experience_req        = models.CharField(max_length=1500, null=True, blank=True)
    additional_req        = models.CharField(max_length=1500, null=True, blank=True)
    job_location          = models.CharField(max_length=1500, null=True, blank=True)
    salaray               = models.IntegerField(null=True, blank=True)
    compensation          = models.CharField(max_length=1500, null=True, blank=True)
    application_deadline  = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    application_procedure = models.CharField(max_length=1500, null=True, blank=True)
    publish_on     	 	  = models.DateTimeField(auto_now=True, auto_now_add=False)
    draft                 = models.BooleanField(default=False)
    slug                  = models.SlugField(unique=True, null=True, blank=True)


    objects = JobPostManager()


    def __str__(self):
        return str(self.position)


    class Meta:
        ordering = ["-publish_on"]


    def get_absolute_url(self):
        return reverse("Employee:home")


    def get_markdown(self):
        job_context = self.job_context
        markdown_text = markdown(job_context)
        return mark_safe(markdown_text)





def create_slug(instance, new_slug=None):
    slug = slugify(instance.position)
    if new_slug is not None:
        slug = new_slug
    qs = Job.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_job_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = create_slug(instance)
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_job_receiver, sender=Job)

