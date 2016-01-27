import json
from rest_framework import viewsets
from rest_framework import status
from rest_framework import renderers
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from celery import shared_task

from common.magento_sync import magento_connect
from .models import ProductAttribute, AttributeSet, Store, CategoryTree, Product
from .serializers import ProductAttributeSerializer, AttributeSetSerializer, StoreSerializer, CategoryTreeSerializer, ProductSerializer
from products.tasks import refresh_products_task, refresh_category_tree_task, refresh_stores_task, refresh_attributes_task

#from .magento_sync import magento_api_instance as magento
import pdb

class AttributeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Attributes to be viewed.
    """
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer


class AttributeSetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Attribute Sets to be viewed.
    """
    queryset = AttributeSet.objects.all()
    serializer_class = AttributeSetSerializer

    @list_route(methods=['get'], renderer_classes=[renderers.StaticHTMLRenderer], url_path='refresh-attribute-sets')
    def refresh_attributes(self, request, *args, **kwargs):
        async_result = refresh_attributes_task.delay()
        return Response(json.dumps({ 'refresh_attributes_data': 'A refresh_attributes_task has been submitted to the queue.'}),
                         status=status.HTTP_200_OK)
 

class StoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Stores to be viewed and edited/created.
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    @list_route(methods=['get'], renderer_classes=[renderers.StaticHTMLRenderer], url_path='refresh-stores')
    def refresh_stores(self, request, *args, **kwargs):
        async_result = refresh_stores_task.delay()
        return Response(json.dumps({ 'refresh_stores_data': 'A refresh_stores_task has been submitted to the queue.'}),
                         status=status.HTTP_200_OK)


class CategoryTreeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows CategoryTree to be viewed.
    """
    queryset = CategoryTree.objects.all()
    serializer_class = CategoryTreeSerializer

    @list_route(methods=['get'], renderer_classes=[renderers.StaticHTMLRenderer], url_path='refresh-category-tree')
    def refresh_category_tree(self, request, *args, **kwargs):
        async_result = refresh_category_tree_task.delay()
        return Response(json.dumps({ 'refresh_category_tree_data': 'A task has been submitted to the queue.'}),
                         status=status.HTTP_200_OK)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Products to be viewed and added/edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @list_route(methods=['get'], renderer_classes=[renderers.StaticHTMLRenderer], url_path='refresh-products')
    def refresh_products(self, request, *args, **kwargs):
        async_result = refresh_products_task.delay()
        return Response(json.dumps({ 'refresh_products_data': 'A task has been submitted to the queue.'}),
                         status=status.HTTP_200_OK)





