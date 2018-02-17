from django.contrib.auth.models import Group
from rest_framework import serializers

from T2API.models import ApiUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiUser
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
