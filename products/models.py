from django.db import models
from customers.models import Relation
from jsonfield import JSONField

from common.utils import SingletonModel

# Magento-related models ==============================================================================
class AttributeSet(models.Model):
    name = models.CharField(max_length=300)
    set_id = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    #attribute = models.ForeignKey(ProductAttribute)
    #attribute_members = models.ManyToManyField(ProductAttribute)

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    code = models.CharField(max_length=100)
    attribute_id = models.CharField(max_length=10, blank=True, null=True)
    required = models.BooleanField(blank=True)
    scope = models.CharField(max_length=20, blank=True, null=True)
    attribute_type = models.CharField(max_length=20, blank=True, null=True)
    attribute_set = models.ForeignKey(AttributeSet)
    magento_attribute_set_id = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.code


class Store(models.Model):
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=100)
    is_active = models.BooleanField()
    group_id = models.CharField(max_length=100)
    sort_order = models.CharField(max_length=100)
    store_id = models.CharField(max_length=100)
    website_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


class ProductDeliveryTime(models.Model):
    days = models.PositiveIntegerField()
    verbose_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.verbose_name


class Product(models.Model):
    SIMPLE = 'simple'
    CONFIGURABLE = 'configurable'
    GROUPED = 'grouped'
    BUNDLE = 'bundle'
    VIRTUAL = 'virtual'
    DOWNLOADABLE = 'downloadable'
    PRODUCT_TYPES = (
                        (SIMPLE, 'Simple'),
                        (CONFIGURABLE, 'Configurable'),
                        (GROUPED, 'Grouped'),
                        (BUNDLE, 'Bundle'),
                        (VIRTUAL, 'Virtual'),
                        (DOWNLOADABLE, 'Downloadable'),
                    )

    attribute_set = models.ForeignKey(AttributeSet, blank=True, null=True)
    product_type = models.CharField(max_length=30, choices=PRODUCT_TYPES, default=CONFIGURABLE)
    stock = models.PositiveIntegerField(blank=True, null=True)
    supplier = models.ForeignKey(Relation, limit_choices_to={'is_supplier': True}, blank=True, null=True)
    minimum_order_quantity = models.PositiveIntegerField(blank=True, null=True)
    delivery_time = models.ForeignKey(ProductDeliveryTime, null=True, blank=True)
    sku = models.CharField('SKU', max_length=120, null=True, blank=True)
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    products_associated_with = models.ManyToManyField('self', blank=True)
    magento_product_id = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.name


class ProductOnlineProperties(models.Model):
    store = models.ForeignKey(Store)
    product = models.ForeignKey(Product)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    available_on_website = models.BooleanField(default=False)
    purchable_from_website = models.BooleanField(default=False)
    name = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    advantage_1 = models.CharField(max_length=120, null=True, blank=True)
    advantage_2 = models.CharField(max_length=120, null=True, blank=True)
    advantage_3 = models.CharField(max_length=120, null=True, blank=True)
    #Category???

    class Meta:
        verbose_name_plural = 'Product online properties'
        unique_together = (("store", "product"),)

    def __str__(self):
        return self.name


class DefaultOnlineProperties(models.Model):
    product = models.ForeignKey(Product)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    available_on_website = models.BooleanField(default=False)
    purchable_from_website = models.BooleanField(default=False)
    name = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    advantage_1 = models.CharField(max_length=120, null=True, blank=True)
    advantage_2 = models.CharField(max_length=120, null=True, blank=True)
    advantage_3 = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Default product online properties'

    def __str__(self):
        return self.name


class CategoryTree(SingletonModel):
    category_tree = JSONField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)


    #associated_with = models.ForeignKey('self', null=True, blank=True)

    #supplier_sku = models.CharField(max_length=120,null=True, blank=True)
    #order_per_X = models.CharField(max_length=10,null=True, blank=True )
    ##supplier_delivery_time= models.CharField(max_length=10,default=7 )
    
    #Meubis_be_Nederlands= models.BooleanField(default=False)
    #Meubis_be_France= models.BooleanField(default=False)
    #Meubis_nl_Nederlads= models.BooleanField(default=False)
    #Horeca= models.BooleanField(default=False)
    #Color= models.CharField(max_length=120,null=True, blank=True )
    #height=models.CharField(max_length=120,null=True, blank=True )
    #width=models.CharField(max_length=120,null=True, blank=True )
    #lenght=models.CharField(max_length=120,null=True, blank=True )
    #weight= models.PositiveIntegerField(blank=True, null=True)

    #size=models.CharField(max_length=120,null=True, blank=True )
    #advantage_1= models.CharField(max_length=120,null=True, blank=True )
    #advantage_2= models.CharField(max_length=120,null=True, blank=True )
    #advantage_3= models.CharField(max_length=120,null=True, blank=True)


    #name = models.CharField(max_length=120)
    #shortdescription = models.TextField(null=True, blank=True)
    #description = models.TextField(null=True, blank=True)
    #price = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    #sale_price = models.DecimalField(decimal_places=2, max_digits=100,
    #                                 null=True, blank=True)
    #slug = models.SlugField(unique=True)

    #active = models.BooleanField(default=True)


# class ProductAssociation(models.Model):
#     product = models.ForeignKey(Product)
#     target_product = models.ForeignKey(Product, related_name='target_product_set')
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = (("product", "target_product"),)



    





# =====================================================================================================


# class Catalog(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=150)
#     description = models.TextField()
#     created_date = models.DateTimeField(auto_now_add=False, auto_now=True)


# class CatalogCategory(models.Model):
#     catalog = models.ForeignKey('Catalog',
#                                 related_name='categories')
#     parent = models.ForeignKey('self', blank=True, null=True,
#                                related_name='children')
#     name = models.CharField(max_length=300)
#     slug = models.SlugField(max_length=150)
#     description = models.TextField(blank=True)


# class Product(models.Model):
#     category = models.ForeignKey('CatalogCategory',
#                                  related_name='products')
#     PRODUCT_CHOICES = (
#         ('simple', 'Simple'),
#         ('configurable', 'Configurable'),
#         ('grouped', 'Grouped'),
#         ('bundle', 'Bundle'),
#     )

#     DEV_CHOICES = (
#         ('3day', 'Three Days'),
#         ('7days', 'Seven Days'),
#         ('14days', 'Fourteen Days'),
#         ('21 Days', 'Twenty One Days'),
#     )

#     GROUP_CHOICES = (
#         ('Default', 'Default'),
#         ('Beds', 'Beds'),

#     )
#     type_product = models.CharField('Product type', max_length=50,
#                                     choices=PRODUCT_CHOICES, default='simple')
#     delivery = models.CharField('Delivery time', max_length=50,
#                                     choices=DEV_CHOICES, default='Please select')
#     groups = models.CharField('Websites', max_length=50,
#                                     choices=GROUP_CHOICES , default='Please select')

#     weight= models.CharField(max_length=10, default=5)
#     stock = models.CharField(max_length=10,null=True, blank=True)
#     supplier= models.CharField(max_length=120,null=True, blank=True)
#     supplier_sku = models.CharField(max_length=120,null=True, blank=True)
#     order_per_X = models.CharField(max_length=10,null=True, blank=True )
#     supplier_delivery_time= models.CharField(max_length=10,default=7 )
#     Meubis_be_Nederlands= models.BooleanField(default=False)
#     Meubis_be_France= models.BooleanField(default=False)
#     Meubis_nl_Nederlads= models.BooleanField(default=False)
#     Horeca= models.BooleanField(default=False)
#     Color= models.CharField(max_length=120,null=True, blank=True )
#     height=models.CharField(max_length=120,null=True, blank=True )
#     width=models.CharField(max_length=120,null=True, blank=True )
#     lenght=models.CharField(max_length=120,null=True, blank=True )

#     size=models.CharField(max_length=120,null=True, blank=True )
#     advantage_1= models.CharField(max_length=120,null=True, blank=True )
#     advantage_2= models.CharField(max_length=120,null=True, blank=True )
#     advantage_3= models.CharField(max_length=120,null=True, blank=True)


#     name = models.CharField(max_length=120)
#     shortdescription = models.TextField(null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#     price = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
#     sale_price = models.DecimalField(decimal_places=2, max_digits=100,
#                                      null=True, blank=True)
#     #slug = models.SlugField(unique=True)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     active = models.BooleanField(default=True)

#     def __unicode__(self):
#         return self.title


#     def get_price(self):
#         return self.price

#     def get_absolute_url(self):
#         return reverse("single_product", kwargs={"slug": self.slug})



# class ProductImage(models.Model):
#     product = models.ForeignKey(Product)
#     image = models.ImageField(upload_to='products/images/')
#     featured = models.BooleanField(default=False)
#     thumbnail = models.BooleanField(default=False)
#     active = models.BooleanField(default=True)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)

#     def __unicode__(self):
#         return self.product.title


# class ProductDetail(models.Model):
#     product = models.ForeignKey('Product',
#                                 related_name='details')
#     attribute = models.ForeignKey('ProductAttribute')
#     value = models.CharField(max_length=500)
#     description = models.TextField(blank=True)

#     def __unicode__(self):
#         return u'%s: %s - %s' % (self.product,
#                                  self.attribute,
#                                  self.value)





# class Mageconnect(models.Model):
#     storeurl = models.TextField(blank=True)
#     key = models.TextField(blank=True)
#     user = models.TextField(blank=True)