from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from ecommerceapi.models import *
from .customers import CustomersSerializer
from .product import ProductSerializer


class CustomerIDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        url = serializers.HyperlinkedIdentityField(
            view_name='customers',
            lookup_field='id'
        )
        fields = ('id',)
        depth = 2


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = CustomerIDSerializer()

    class Meta:
        model = Order
        url = serializers.HyperlinkedIdentityField(
            view_name='order',
            lookup_field='id'
        )
        fields = ('id', 'payment_type', 'url', 'customer')

        depth = 2


class Orders(ViewSet):

    def destroy(self, request, pk=None):
        try:
            open_order = Order.objects.get(pk=pk)
            open_order.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        order = Order.objects.get(pk=pk)
        order.payment_type_id = request.data["payment_type_id"]
        order.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        # Checking for open order here
        customer = Customer.objects.get(user=request.user.id)
        current_order = Order.objects.filter(
            customer=customer, payment_type=None)
        # print("Current Order:", current_order[0].id)
        print("q******", current_order.values_list)
        if len(current_order) == 0:
            print("Current Order:", current_order)
            new_order = Order()
            new_order.customer = customer
            new_order.payment_type = None
            new_order.save()

            new_order_product = OrderProduct()

            product = Product.objects.get(pk=request.data["product_id"])
            # payment_type = PaymentType.objects.get(
            #     pk=request.data["payment_type_id"])
            new_order_product.product = product
            new_order_product.order = new_order
            new_order_product.save()

            serializer = OrderSerializer(
                new_order, context={'request': request}
            )
            return Response(serializer.data)

        elif current_order[0].id != 0:
            order_product = OrderProduct()
            # product = Product.objects.get(pk=request.data["product_id"])
            order_product.product_id = request.data["product_id"]
            order_product.order = current_order[0]
            order_product.save()
            products_on_order = Product.objects.filter(
                cart__order=current_order[0])

            serializer = ProductSerializer(
                products_on_order, many=True, context={'request': request}
            )

            return Response(serializer.data)

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
