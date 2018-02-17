from django.contrib.auth.models import AbstractUser
from django.db import models


class ApiUser(AbstractUser):
    pass


class Product(models.Model):
    name = models.CharField(max_length=150)
    ean = models.CharField(max_length=13)

    def __str__(self):
        return self.name


# Create your models here.
class Device(models.Model):
    mac = models.CharField(max_length=12, unique=True)
    secret_key = models.TextField
    pollingRate = models.IntegerField
    resolution = models.CharField(max_length=15)
    last_ping = models.DateTimeField(auto_now=True)
    battery_status = models.CharField(max_length=20)

    user = models.ForeignKey(ApiUser, related_name='devices', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='devices', on_delete=models.PROTECT)

    def __str__(self):
        return self.mac

    class Meta:
        ordering = ('mac',)
        permissions = (
            'show_status',
            'register_device',
            'change_device',
            'change_product'
        )
