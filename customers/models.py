from django.db import models


# class Customer(models.Model):
#     email = models.CharField(max_length=150, unique=True,blank=True)
#     name  = models.CharField(max_length=150,blank=True )
#     address = models.ForeignKey('CustomerAddress')
#     phone_number = models.CharField(max_length=12 ,blank=True)

class Address(models.Model):

    class Meta:
        verbose_name_plural = "addresses"

    line_1 = models.CharField(max_length=300, blank=True, null=True)
    line_2 = models.CharField(max_length=300, blank=True, null=True)
    line_3 = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    postcode = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    region = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    country_id = models.CharField(max_length=100, blank=True, null=True)
    magento_customer_address_id = models.CharField(max_length=100, blank=True, null=True)
    magento_region_id = models.CharField(max_length=100, blank=True, null=True)
    magento_is_default_billing = models.BooleanField(default=False)
    magento_is_default_shipping = models.BooleanField(default=False)

    def __str__(self):
        return '{street_name} {city}'.format(street_name=self.line_1, city=self.city)


class Relation(models.Model):
    # CLIENT = 'client'
    # SUPPLIER = 'supplier'
    # RELATION_TYPES = (
    #                     (CLIENT, 'Client'),
    #                     (SUPPLIER, 'Supplier'),
    #                  )

    #relation_type = models.CharField(max_length=30, choices=RELATION_TYPES, blank=False, null=False)
    is_client = models.BooleanField('is client', default=False)
    is_supplier = models.BooleanField('is supplier', default=False)
    name = models.CharField('name', max_length=300, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(verbose_name='email address', max_length=255, blank=True, null=True)
    is_active = models.BooleanField('active', default=True)
    vat_number = models.CharField('vat number', max_length=100, blank=True, null=True)
    addresses = models.ManyToManyField(Address, blank=True)
    sku = models.CharField('SKU', max_length=120, blank=True, null=True)
    magento_customer_id = models.CharField(max_length=100, blank=True, null=True)
    magento_default_billing = models.CharField(max_length=100, blank=True, null=True)
    magento_default_shipping = models.CharField(max_length=100, blank=True, null=True)
    magento_group_id = models.CharField(max_length=100, blank=True, null=True)
    magento_store_id = models.CharField(max_length=100, blank=True, null=True)
    magento_website_id = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name

    