import json
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from rest_framework import viewsets
from rest_framework import status
from rest_framework import renderers
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from common.magento_sync import magento_connect
from .models import Address, Relation
from .serializers import AddressSerializer, RelationSerializer
from customers.tasks import refresh_relations_task


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Addresses to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class RelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Relations to be viewed or edited.
    """
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer

    @list_route(methods=['get'], renderer_classes=[renderers.StaticHTMLRenderer], url_path='refresh-relations')
    def refresh_relations(self, request, *args, **kwargs):
        async_result = refresh_relations_task.delay()
        return Response(json.dumps({ 'refresh_relations_data': 'A refresh_relations_task has been submitted to the queue.'}),
                         status=status.HTTP_200_OK)


