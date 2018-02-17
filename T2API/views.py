import datetime

from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import detail_route
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from T2API.models import ApiUser, Product, Device
from T2API.serializers import UserSerializer, GroupSerializer, DeviceSerializer, ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ApiUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UaDeviceViewSet(DeviceViewSet):
    permission_classes = (permissions.AllowAny,)

    @detail_route(methods=['GET', 'POST'], permission_classes=(permissions.AllowAny,), url_name='weight')
    def weight(self, request, pk=None):
        queryset = Device.objects.all()
        device = get_object_or_404(queryset, pk=pk)

        if request.method == 'GET':
            serializer = DeviceSerializer(device, context={'request': request})
            return Response({'weight': serializer.data.get('last_weight')})

        elif request.method == 'POST':
            serializer = DeviceSerializer(device, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                device.last_weight = request.data['last_weight']
                device.save()
                return Response({'status': 'success'})
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['POST'], permission_classes=(permissions.AllowAny,), url_name='register')
    def register(self, request, pk=None):
        # TODO
        queryset = Device.objects.all()
        device = get_object_or_404(queryset, pk=pk)

        mac = request.data['mac']
        initial_data = {
            'mac': mac
        }

        serializer = DeviceSerializer(device, data=initial_data, partial=True, context={'request': request})
        if serializer.is_valid():
            device = serializer.data
            device.save()
            return Response({'status': 'success'})
        else:
            return Response(serializer.errors, )

    @detail_route(methods=['POST'], permission_classes=(permissions.AllowAny,), url_name='ping')
    def ping(self, request, pk=None):
        queryset = Device.objects.all()
        device = get_object_or_404(queryset, pk=pk)

        last_ping = datetime.datetime.now()
        device.last_ping = last_ping
        device.save()
        return Response({'status': 'success'})

    @detail_route(methods=['GET', 'POST'], permission_classes=(permissions.AllowAny,), url_name='battery')
    def battery_status(self, request, pk=None):
        queryset = Device.objects.all()
        device = get_object_or_404(queryset, pk=pk)

        if request.method == 'GET':
            serializer = DeviceSerializer(device, context={'request': request})
            return Response({'battery_status': serializer.data.get('battery_status')})

        elif request.method == 'POST':
            serializer = DeviceSerializer(device, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                device.battery_status = request.data['battery_status']
                device.save()
                return Response({'status': 'success'})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['GET'], permission_classes=(permissions.AllowAny,), url_name='product_weight')
    def product_weight(self, request, pk=None):
        queryset = Device.objects.all()
        device = get_object_or_404(queryset, pk=pk)

        serializer = ProductSerializer(device.product, context={'request': request})
        return Response({'product_weight': serializer.data.get('weight')})


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
