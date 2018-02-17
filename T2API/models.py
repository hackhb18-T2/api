from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150)
    ean = models.CharField(max_length=13)

# Create your models here.
class Device(models.Model):
    mac = models.CharField(max_length=12, unique=True)
    secret_key = models.TextField
    pollingRate = models.IntegerField
    resolution = models.CharField(max_length=15)
    last_ping = models.DateTimeField(auto_now=True)
    battery_status = models.CharField(max_length=20)

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
