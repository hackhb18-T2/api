from django.contrib.auth.models import AbstractUser
from django.db import models


class ApiUser(AbstractUser):
    deviceUser = models.BooleanField(default=False)
    pass


class Product(models.Model):
    name = models.CharField(max_length=150)
    ean = models.CharField(max_length=13)

    def __str__(self):
        return self.name


# Create your models here.
class Device(models.Model):
    mac = models.CharField(max_length=12, unique=True)
    secret_key = models.TextField(null=True, default=None)
    polling_rate = models.IntegerField(null=True)
    resolution = models.CharField(max_length=15, default=None, null=True)
    last_ping = models.DateTimeField(auto_now=True)
    battery_status = models.CharField(max_length=20, default=None, null=True)

    user = models.ForeignKey(ApiUser, related_name='devices', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='devices', on_delete=models.PROTECT, null=True, default=None)

    def __str__(self):
        return self.mac

    class Meta:
        ordering = ('mac',)
        permissions = (
            ('show_status', 'Can show status vars'),
            ('register_device', 'Can register a device'),
            ('change_product', 'Can change associated procduct'),
        )
