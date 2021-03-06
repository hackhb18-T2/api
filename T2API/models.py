from django.contrib.auth.models import AbstractUser
from django.db import models


class ApiUser(AbstractUser):
    deviceUser = models.BooleanField(default=False)
    pass


# Ignore
class ProductCategory(models.Model):
    name = models.CharField(null=False, max_length=50)
    type = models.CharField(null=False, default='primary', max_length=25)  # primary, matching
    order = models.IntegerField(null=False, default=0)  # in category

    def __str__(self):
        return self.name


class Product(models.Model):
    # FullDepth
    name = models.CharField(max_length=150)
    ean = models.CharField(max_length=13)

    weight = models.IntegerField(null=True, default=None)
    image_url = models.TextField(null=True, default=None)

    # category

    def __str__(self):
        return self.name


class PriceOffer(models.Model):
    seller = models.CharField(null=False, max_length=250)  # Identifier
    name = models.CharField(null=False, max_length=250)  # RealName
    price = models.FloatField(null=False)  # Price
    vat = models.IntegerField(null=True, default=7)
    image_url = models.TextField(null=True, default=None)

    prices = models.ForeignKey(Product, related_name='prices', on_delete=models.CASCADE, null=True)  # List<PriceOffer>

    def __str__(self):
        return '{} ({})'.format(self.name, self.seller)


class ProductHistory(models.Model):
    # ordered : bool
    # -> product
    # -> device
    # timestamp
    pass


# class NotificationTarget(models.Model):
# warning_target
# error_target
# devices []
#    pass

class Notification(models.Model):
    # description
    # seen?
    # timestamp
    # type (outOfStock, battery)
    pass


# Create your models here.
class Device(models.Model):
    mac = models.CharField(max_length=12, unique=True)
    secret_key = models.TextField(null=True, default=None)
    polling_rate = models.IntegerField(null=True)
    resolution = models.IntegerField(default=10)
    last_ping = models.DateTimeField(default=None, null=True)
    battery_status = models.CharField(max_length=20, default=None, null=True)
    last_weight = models.IntegerField(null=False, default=-1)

    # notification_target
    # auto_order?
    # history : ProductHistory
    # target_amount
    # active_amount

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
