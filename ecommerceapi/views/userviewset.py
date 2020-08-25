from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name='users',
            lookup_field='id'
        )
        fields = ('id', 'url', 'first_name', 'last_name', 'email')


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
