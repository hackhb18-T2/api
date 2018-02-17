from django.contrib.auth.models import Group
from rest_framework import serializers

from T2API.models import ApiUser, Device


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiUser
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('mac', 'polling_rate', 'resolution', 'last_ping', 'battery_status')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('name', 'ean')
