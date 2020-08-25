"""bangazonllc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from ecommerceapi.models import ProductType
from ecommerceapi.views import ProductTypes
from ecommerceapi.models import Customer
from ecommerceapi.views import Customers
from ecommerceapi.views import UserViewSet
from ecommerceapi.models import PaymentType
from ecommerceapi.views import PaymentTypes

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'producttypes', ProductTypes, 'producttype')
router.register(r'customers', Customers, 'customer')
router.register(r'users', UserViewSet, 'user')
router.register(r'paymenttypes', PaymentTypes, 'paymenttype')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('register/', register_user),
    # path('login/', login_user),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
