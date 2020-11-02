from django.contrib import admin
from .models import Portfulio, Address, SocialLink, Employee, FollowRequest

admin.site.register(FollowRequest) 

# Register your models here.

admin.site.register(Employee)
admin.site.register(Portfulio)

admin.site.register(Address)
admin.site.register(SocialLink)


# class ProductImageInline(admin.TabularInline):
#     model = ProductImage
#     extra = 3



# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ ProductImageInline]
    
# admin.site.register(Product, ProductAdmin)