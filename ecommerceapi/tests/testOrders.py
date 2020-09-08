import json
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.test import TestCase
from django.urls import reverse
from ecommerceapi.models import *
from django.contrib.auth.models import User


class TestOrder(TestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'user_test'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.customer = Customer.objects.create(
            address="123 Down Way", phone_number="222-222-2222", user=self.user)
        self.product_type = ProductType.objects.create(name="Whizzles")
        self.product = Product.objects.create(title="prod", customer=self.customer, price=5.99, description="Stuff",
                                              quantity=1, location="Nashville", imagePath="image_path", product_type=self.product_type)
        self.order = Order.objects.create(
            customer=self.customer)

    def tearDown(self):
        self.username = 'tester'
        self.password = 'user_test'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.customer = Customer.objects.create(
            address="123 Down Way", phone_number="222-222-2222", user=self.user)
        self.order = Order.objects.create(customer=self.customer)

    def test_post_order(self):

        product = {
            "product_id": self.product.id,

        }

        response = self.client.post(
            reverse('order-list'), product, HTTP_AUTHORIZATION='Token ' + str(self.token)
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(Order.objects.count(), 1)

        self.assertEqual(Order.objects.get().customer.address, '123 Down Way')

    # def test_delete_order(self):

    #     order = {
    #         "order_id": self.order.id
    #     }

    #     url = reverse('orders-delete', kwargs={'order_id': self.order.id})
    #     #   HTTP_AUTHORIZATION='Token ' + str(self.token)
    #     response = self.client.delete(url)

    #     self.assertEqual(response.status_code, 200)

    #     self.assertEqual(Order.objects.count(), 0)
