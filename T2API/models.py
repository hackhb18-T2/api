from django.contrib.auth.models import AbstractUser
from django.db import models


class ApiUser(AbstractUser):
    deviceUser = models.BooleanField(default=False)
    pass


# Ignore
class ProductCategory(models.Model):
    name = models.CharField(null=False),
    type = models.CharField(null=False, default='primary'),  # primary, matching
    order = models.IntegerField(null=False, default=0)  # in category

    def __str__(self):
        return self.name


class PriceOffer(models.Model):
    seller = models.CharField(null=False),  # Identifier
    name = models.CharField(null=False),  # RealName
    price = models.FloatField(null=False),  # Price
    vat = models.IntegerField(null=True, default=7),
    image_url = models.TextField(null=False, default=None)

    def __str__(self):
        return self.name


class Product(models.Model):
    # FullDepth
    name = models.CharField(max_length=150)
    ean = models.CharField(max_length=13)

    weight = models.IntegerField(null=True, default=None)
    prices = models.ForeignKey(PriceOffer, related_name='Product', on_delete=models.CASCADE),  # List<PriceOffer>
    image_url = models.TextField(null=True, default=None),

    # category

    def __str__(self):
        return self.name


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
