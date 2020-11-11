from django.contrib import admin
from .models import Job, Category
from pagedown.widgets import AdminPagedownWidget

# Register your models here.

from django.db import models



class JobAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }


admin.site.register(Job, JobAdmin) 
admin.site.register(Category) 
