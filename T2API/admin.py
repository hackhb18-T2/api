from django.contrib import admin

from .models import Product, Device, ApiUser

# Register your models here.
admin.site.register(ApiUser)

admin.site.register(Product)
admin.site.register(Device)
