from django.contrib.auth.models import Group
from rest_framework import serializers

from T2API.models import ApiUser, Device, Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiUser
        fields = ('url', 'username', 'email', 'groups', 'devices')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('url', 'name', 'ean', 'weight')


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    # product = serializers.HyperlinkedModelSerializer(read_only=False, required=False)
    # user = serializers.ReadOnlyField(source='user.username')
    # user = serializers.SlugRelatedField(slug_field='username', required=True, queryset=UserSerializer)

    class Meta:
        model = Device
        fields = ('url', 'mac', 'polling_rate',
                  'resolution', 'last_ping',
                  'battery_status', 'user', 'product',
                  'last_weight'
                  )
        depth = 0
