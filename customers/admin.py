from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from .models import Address, Relation


class AddressResource(resources.ModelResource):

    class Meta:
        model = Address
        exclude = None

class AddressAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'line_1', 'line_2', 'line_3', 'city', 'postcode', 'state', 'country')
    resource_class = AddressResource

admin.site.register(Address, AddressAdmin)


class RelationResource(resources.ModelResource):

    class Meta:
        model = Relation
        exclude = None

class RelationAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'magento_customer_id', 'name', 'email', 'company', 'phone_number', 'is_client', 'is_supplier')
    resource_class = RelationResource

admin.site.register(Relation, RelationAdmin)
