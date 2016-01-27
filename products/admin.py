from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
import products.models as products_models 


class ProductAttributeResource(resources.ModelResource):
    class Meta:
        model = products_models.ProductAttribute
        exclude = None
class ProductAttributeAdmin(ImportExportActionModelAdmin):
    list_display = ( 'id', 'code', 'attribute_id', 'required', 'scope',
                     'attribute_type', 'created_at', 'updated_at')
    resource_class = ProductAttributeResource
admin.site.register(products_models.ProductAttribute, ProductAttributeAdmin)


class AttributeSetResource(resources.ModelResource):
    class Meta:
        model = products_models.AttributeSet
        exclude = None
class AttributeSetAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name', 'set_id', 'created_at', 'updated_at')
    resource_class = AttributeSetResource
admin.site.register(products_models.AttributeSet, AttributeSetAdmin)


class StoreResource(resources.ModelResource):
    class Meta:
        model = products_models.Store
        exclude = None
class StoreAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'code', 'is_active', 'store_id', 'website_id', 'created_at', 'updated_at')
    resource_class = StoreResource
admin.site.register(products_models.Store, StoreAdmin)


class ProductOnlinePropertiesResource(resources.ModelResource):
    class Meta:
        model = products_models.ProductOnlineProperties
        exclude = None
class ProductOnlinePropertiesAdmin(ImportExportActionModelAdmin):
    resource_class = ProductOnlinePropertiesResource
admin.site.register(products_models.ProductOnlineProperties, ProductOnlinePropertiesAdmin)


class DefaultOnlinePropertiesResource(resources.ModelResource):
    class Meta:
        model = products_models.DefaultOnlineProperties
        exclude = None
class DefaultOnlinePropertiesAdmin(ImportExportActionModelAdmin):
    resource_class = DefaultOnlinePropertiesResource
admin.site.register(products_models.DefaultOnlineProperties, DefaultOnlinePropertiesAdmin)


class ProductResource(resources.ModelResource):
    class Meta:
        model = products_models.Product
        exclude = None
class ProductAdmin(ImportExportActionModelAdmin):
    resource_class = ProductResource
admin.site.register(products_models.Product, ProductAdmin)


class ProductDeliveryTimeResource(resources.ModelResource):
    class Meta:
        model = products_models.ProductDeliveryTime
        exclude = None
class ProductDeliveryTimeAdmin(ImportExportActionModelAdmin):
    resource_class = ProductDeliveryTimeResource
admin.site.register(products_models.ProductDeliveryTime, ProductDeliveryTimeAdmin)


class CategoryTreeResource(resources.ModelResource):
    class Meta:
        model = products_models.CategoryTree
        exclude = None
class CategoryTreeAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'category_tree', 'created_at', 'updated_at')
    resource_class = CategoryTreeResource
admin.site.register(products_models.CategoryTree, CategoryTreeAdmin)

# class RelationResource(resources.ModelResource):

#     class Meta:
#         model = Relation
#         exclude = None

# class RelationAdmin(ImportExportActionModelAdmin):
#     list_display = ('id', 'relation_type', 'name', 'company', 'phone_number', 'email', 
#                     'is_active', 'vat_number', 'address')
#     resource_class = RelationResource

# admin.site.register(Relation, RelationAdmin)


# class MageconnectAdimn (admin.ModelAdmin):
#     list_display = ('storeurl', 'key', 'user')
# admin.site.register(Mageconnect, MageconnectAdimn )

# class CatalogAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
# admin.site.register(Catalog, CatalogAdmin)

# class CatalogCategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'parent')
# admin.site.register(CatalogCategory, CatalogCategoryAdmin)

#class ProductAdmin(admin.ModelAdmin):
   # list_display = ('type_product', 'name', 'description', 'category')
    #prepopulated_fields = {'slug': ('name',)}
#admin.site.register(Product, ProductAdmin)

#class ProductDetailAdmin(admin.ModelAdmin):
    #list_display = ('category', 'product', 'attribute', 'value')
#admin.site.register(ProductDetail, ProductDetailAdmin)
