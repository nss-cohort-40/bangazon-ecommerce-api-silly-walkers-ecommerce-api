from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from ecommerceapi.models import *


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        url = serializers.HyperlinkedIdentityField(
            view_name='order',
            lookup_field='id'
        )
        fields = ('id', 'url', 'customer')

        depth = 1


class Orders(ViewSet):

    def create(self, request):

        new_order = Order()
        new_order.create_date = request.data["create_date"]

        customer = Customer.objects.get(pk=request.data["customer_id"])
        # payment_type = PaymentType.objects.get(
        #     pk=request.data["payment_type_id"])
        new_order.customer = customer
        # new_order.payment_type = payment_type
        new_order.save()

    def retrieve(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        orders = Order.objects.all()
        # Filtering for orders by customer id
        customer = self.request.query_params.get('customer', None)
        if customer is not None:
            orders = orders.filter(customer__id=customer)

        serializer = OrderSerializer(
            orders, many=True, context={'request': request}
        )
        return Response(serializer.data)
