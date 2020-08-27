from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ecommerceapi.models import Product
from ecommerceapi.models import ProductType
from ecommerceapi.models import Customer 


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        url = serializers.HyperlinkedIdentityField(
            view_name='product',
            lookup_field='id'
        )
        fields = ('id', 'url', 'title', 'quantity', 'price', 'description', 'customer', 'imagePath', 'location', 'product_type')
        depth= 1


class Products(ViewSet):

    def create(self, request):
        new_product = Product()
        product_type = Product.objects.get(pk=request.data["producttype_id"])
        customer = Customer.objects.get(user=request.auth.user)
        
        new_product.title = request.data["title"]
        new_product.description = request.data["description"]
        new_product.quantity = request.data["quantity"]
        new_product.location = request.data["location"]
        new_product.imagePath = request.data["imagePath"]
        new_product.price = request.data["price"]
        new_product.customer = customer
        new_product.product_type = product_type
        
        new_product.save()

        serializer = ProductSerializer(new_product, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def destroy(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(
            products, many=True, context={'request': request})
        return Response(serializer.data)
