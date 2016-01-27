from __future__ import absolute_import
from celery import shared_task

from common.magento_sync import magento_connect
from .models import Address, Relation


def get_address_obj(address):
    updated_values = {  'line_1': address.get('street'),
                        'city': address.get('city'),
                        'postcode': address.get('postcode'),
                        'region': address.get('region'),
                        'country_id': address.get('country_id'),
                        'magento_customer_address_id': address.get('customer_address_id'),
                        'magento_region_id': address.get('region_id'),
                        'magento_is_default_billing': address.get('is_default_billing'),
                        'magento_is_default_shipping': address.get('is_default_shipping'),
                     }

    address_obj, address_created = Address.objects.update_or_create(
                                        magento_customer_address_id=address.get('customer_address_id'),
                                        defaults=updated_values)
    if address_obj:
        return address_obj
    else:
        return None


@shared_task
def refresh_relations_task():
    relation_created_num = 0
    address_updated_num = 0
    magento = magento_connect()
    customer_list = magento.customer.list()

    if customer_list:
        for customer in customer_list:
            if customer.get('customer_id'):
                #customer_info = magento.customer.info(int(customer['customer_id']))

                # Create or update the addresses first.
                if int(customer.get('default_shipping', 0)):
                    shipping_address =  magento.customer_address.info(int(customer['default_shipping']))
                    shipping_address_obj = get_address_obj(shipping_address)
                else: 
                    shipping_address_obj = None

                if int(customer.get('default_billing', 0)):
                    billing_address =  magento.customer_address.info(int(customer['default_billing']))
                    billing_address_obj = get_address_obj(billing_address)
                else:
                    billing_address_obj = None

                updated_values = {  'name': customer.get('firstname') + ' ' + customer.get('lastname'),
                                    'phone_number': customer.get('telephone'),
                                    'email': customer.get('email'),
                                    'magento_customer_id': customer.get('customer_id'),
                                    'magento_default_billing': customer.get('default_billing'),
                                    'magento_default_shipping': customer.get('default_shipping'),
                                    'magento_group_id': customer.get('group_id'),
                                    'magento_store_id': customer.get('store_id'),
                                    'magento_website_id': customer.get('website_id'),
                                 }  

                relation_obj, relation_created = Relation.objects.update_or_create(
                                                    magento_customer_id=customer.get('customer_id'),
                                                    defaults=updated_values)

                if relation_created:
                    relation_created_num += 1

                # Add foreign keys to shipping and billing addresses
                if shipping_address_obj:
                    address_updated_num += 1
                    relation_obj.addresses.add(shipping_address_obj)

                if billing_address_obj:
                    address_updated_num += 1
                    relation_obj.addresses.add(billing_address_obj)

    response_object = { 'relation_created_num': relation_created_num,
                        'address_updated_num': address_updated_num }
                        
    return response_object

