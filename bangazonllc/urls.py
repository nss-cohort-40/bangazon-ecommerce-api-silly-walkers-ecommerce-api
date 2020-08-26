from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from ecommerceapi.models import Customer
from ecommerceapi.models import ProductType
from ecommerceapi.views import Customers
from ecommerceapi.views import ProductTypes
from ecommerceapi.views import register_user, login_user
from ecommerceapi.views import UserViewSet
from ecommerceapi.views import Product
from ecommerceapi.models import PaymentType
from ecommerceapi.views import PaymentTypes

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'producttypes', ProductTypes, 'producttype')
router.register(r'customers', Customers, 'customer')
router.register(r'users', UserViewSet, 'user')
router.register(r'product', Products, 'product')
router.register(r'paymenttypes', PaymentTypes, 'paymenttype')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register/', register_user),
    path('login/', login_user),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
