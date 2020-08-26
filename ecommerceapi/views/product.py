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
        fields = ('id', 'url', 'title', 'account_number', 'quantity', 'description' 'created_at', 'customer', 'product_type_Id', 'imagePath')
        depth= 1


class Products(ViewSet):

    def create(self, request):
        new_product = Product()
        new_product.title = request.data["title"]
        new_product.description = request.data["description"]
        new_product.quantity = request.data["quantity"]
        new_product.account_number = request.data["account_number"]
        new_product.customer = request.data["customer"]
        location = Product.objects.get(pk=request.data["product_id"])
        imagePath = Product.objects.get(pk=request.data["imagePath"])
        new_product.created_at = request.data["created_at"]
        product.location = location
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

    def update(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        location = ProductLocation.objects.get(pk=request.data["location_id"])
        product.title = request.data["title"]
        product.created_at = request.data["created_at"]
        product.location = location
        product.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            location.delete()
            product.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        products = Product.objects.all()
        location = self.request.query_params.get('location', None)
        if location is not None:
            products = products.filter(location__id=location)
        serializer = ProductSerializer(
            products, many=True, context={'request': request})
        return Response(serializer.data)
