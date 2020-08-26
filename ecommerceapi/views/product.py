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
        fields = ('id', 'url', 'merchant_name', 'account_number', 'expiration_date', 'created_at', 'customer', 'product_type_Id')
        depth= 1


class Products(ViewSet):

    def create(self, request):
        new_product = Product()
        new_product.name = request.data["name"]
        location = Product.objects.get(pk=request.data["product_id"])
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
        product.name = request.data["name"]
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
