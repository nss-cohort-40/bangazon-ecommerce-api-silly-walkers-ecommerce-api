from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ecommerceapi.models import Customer
from django.contrib.auth.models import User
from .userviewset import UserSerializer


class CustomersSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Customer
        url = serializers.HyperlinkedIdentityField(
            view_name='customers',
            lookup_field='id'
        )
        fields = ('id', 'url', 'user_id', 'address', 'phone_number', 'user')


class Customers(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomersSerializer(
                customer, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        customer = Customer.objects.get(pk=pk)
        user = User.objects.get(customer=pk)
        customer.address = request.data["address"]
        customer.phone_number = request.data["phone_number"]
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        customer.save()
        user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            newcustomer = Customer.objects.get(pk=pk)
            newcustomer.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Customer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        customers = Customer.objects.all()
        serializer = CustomersSerializer(
            customers, many=True, context={'request': request})
        return Response(serializer.data)
