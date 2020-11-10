from django.contrib import admin
from .models import Portfulio, Address, SocialLink, Employee, FollowRequest

admin.site.register(FollowRequest) 

# Register your models here.

admin.site.register(Employee)

admin.site.register(Address)
admin.site.register(SocialLink)


# class PortfulioFileInline(admin.TabularInline):
#     model = Portfulio
#     extra = 3



# class PortfulioAdmin(admin.ModelAdmin):
#     inlines = [ PortfulioFileInline]
    
admin.site.register(Portfulio)
