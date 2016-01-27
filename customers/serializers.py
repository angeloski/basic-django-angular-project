from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Relation, Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'line_1', 'line_2', 'line_3', 'city', 'postcode', 'state', 'country')


class RelationSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(required=False, many=True)

    class Meta:
        model = Relation
        fields = ('id', 'name', 'email', 'phone_number', 'company', 'vat_number', 'sku',
                  'is_client', 'is_supplier', 'is_active', 'addresses')
        depth = 2
