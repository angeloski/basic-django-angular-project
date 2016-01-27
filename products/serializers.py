from rest_framework import serializers
from customers.serializers import RelationSerializer
from .models import ProductAttribute, AttributeSet, Store, CategoryTree, ProductDeliveryTime, Product
import pdb

class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = ('id', 'code', 'attribute_id', 'required', 'scope', 'attribute_type')


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'code', 'is_active', 'group_id', 'sort_order', 'store_id', 'website_id')


class AttributeSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeSet
        fields = ('id', 'name', 'set_id')


class CategoryTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTree
        fields = ('id', 'category_tree')


class ProductDeliveryTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDeliveryTime
        fields = ('id', 'days', 'verbose_name')


class ProductSerializer(serializers.ModelSerializer):
    attribute_set = AttributeSetSerializer()
    supplier = RelationSerializer()
    delivery_time = ProductDeliveryTimeSerializer()

    class Meta:
        model = Product
        fields = ('id', 'attribute_set', 'product_type', 'stock', 'supplier',
                  'minimum_order_quantity', 'delivery_time', 'sku', 'name', 'created_at', 
                  'updated_at', 'products_associated_with')
        depth = 1

#pdb.set_trace()
#ProductSerializer._declared_fields['products_associated_with'] = ProductSerializer()

