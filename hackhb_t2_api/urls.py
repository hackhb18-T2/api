"""hackhb_t2_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from T2API import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'devices', views.DeviceViewSet)
router.register(r'products', views.ProductViewSet)

device_weight = views.DeviceViewSet.as_view({
    'get': 'get_weight'
})

device_register = views.DeviceViewSet.as_view({
    'post': 'register'
})

device_ping = views.DeviceViewSet.as_view({
    'post': 'ping'
})

device_battery = views.DeviceViewSet.as_view({
    'get': 'get_battery',
    'post': 'post_battery'
})

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
                  url(r'^', include(router.urls)),

                  url(r'^device/weight', device_weight),
                  url(r'^device/register', device_register),
                  url(r'^device/ping', device_ping),
                  url(r'^device/battery', device_battery),

                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  url(r'^api-token-auth/', obtain_jwt_token),
                  url(r'^api-token-verify/', verify_jwt_token),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
