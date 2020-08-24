from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ecommerceapi.models import ProductType


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductType
        url = serializers.HyperlinkedIdentityField(
            view_name='producttype',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name')


class ProductTypes(ViewSet):

    def create(self, request):
        newproducttype = ProductType()
        newproducttype.name = request.data["name"]
        newproducttype.save()

        serializer = ProductTypeSerializer(
            newproducttype, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            producttype = ProductType.objects.get(pk=pk)
            serializer = ProductTypeSerializer(
                producttype, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        producttype = ProductType.objects.get(pk=pk)
        producttype.name = request.data["name"]
        producttype.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            producttype = ProductType.objects.get(pk=pk)
            producttype.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ProductType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        producttype = ProductType.objects.all()
        serializer = ProductTypeSerializer(
            producttype, many=True, context={'request': request})
        return Response(serializer.data)
