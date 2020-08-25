from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ecommerceapi.models import PaymentType

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        url = serializers.HyperlinkedIdentityField(
            view_name='paymenttype',
            lookup_field='id'
        )
        fields = ('id', 'url', 'merchant_name', 'account_number', 'expiration_date', 'created_at')


class PaymentTypes(ViewSet):

    def create(self, request):
        newpaymenttype = PaymentType()
        newpaymenttype.merchant_name = request.data["merchant_name"]
        newpaymenttype.account_number = request.data["account_number"]
        newpaymenttype.expiration_date = request.data["expiration_date"]
        newpaymenttype.created_at = request.data["created_at"]
        newpaymenttype.save()

        serializer = PaymentTypeSerializer(
            newpaymenttype, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            paymenttype = PaymentType.objects.get(pk=pk)
            serializer = PaymentTypeSerializer(
                paymenttype, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        paymenttype = PaymentType.objects.get(pk=pk)
        paymenttype.merchant_name = request.data["merchant_name"]
        paymenttype.account_number = request.data["account_number"]
        paymenttype.expiration_date = request.data["expiration_date"]
        paymenttype.created_at = request.data["created_at"]
        paymenttype.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            paymenttype = PaymentType.objects.get(pk=pk)
            paymenttype.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except PaymentType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        paymenttype = PaymentType.objects.all()
        serializer = PaymentTypeSerializer(
            paymenttype, many=True, context={'request': request})
        return Response(serializer.data)
