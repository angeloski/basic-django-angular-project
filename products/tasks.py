from __future__ import absolute_import
from celery import shared_task

from common.magento_sync import magento_connect
from .models import Product, CategoryTree, Store, AttributeSet, ProductAttribute


@shared_task
def refresh_products_task():
    products_created_num = 0
    magento = magento_connect()
    product_list = magento.catalog_product.list()

    if product_list:
        for product in product_list:

            updated_values = {  'name': product.get('name', 'No name specified'),
                                'magento_product_id': product.get('product_id'),
                                'sku': product.get('sku'),
                                'product_type': product.get('type'),
                             }


            obj, created = Product.objects.update_or_create(magento_product_id=product.get('product_id'),
                                                            defaults=updated_values)
            if created:
                products_created_num += 1

    response_object = { 'products_created_num': products_created_num}
    return response_object


@shared_task
def refresh_category_tree_task():
    magento = magento_connect()
    category_tree = magento.catalog_category.tree()

    if category_tree:
        category_tree_object = CategoryTree.load()
        CategoryTree.objects.update_or_create(id=category_tree_object.id, defaults={'category_tree': category_tree})
        response_object = {'Category tree refreshed successfully.'}
    else:
        response_object = {'No category tree was retrieved from Magento.'}

    return response_object

@shared_task
def refresh_stores_task():
    magento = magento_connect()
    store_list = magento.core_store.list()
    stores_created_num = 0
    stores_total = len(store_list)

    if store_list:
        for store in store_list:
            obj, created = Store.objects.update_or_create(store_id=store['store_id'],
                                                          defaults=store)
            if created:
                stores_created_num += 1

    response_object = { 'stores_total': stores_total,
                        'stores_created_num': stores_created_num }
    return response_object


def check_attribute(attribute_info):
    try:
        if (attribute_info['scope'] == 'global' and 
            attribute_info['is_configurable'] == '1' and 
            attribute_info['frontend_input'] == 'select'):
            return True
        else:
            return False
    except:
        return False


@shared_task
def refresh_attributes_task():
    magento = magento_connect()
    attribute_set_list = magento.catalog_product_attribute_set.list()
    sets_created_num = 0
    attribute_created_num = 0
    sets_total = len(attribute_set_list)

    if attribute_set_list:
        for attribute_set in attribute_set_list:
            attribute_set_obj, created = AttributeSet.objects.update_or_create(
                                            set_id=attribute_set.get('set_id'),
                                            defaults=attribute_set)

            if created:
                sets_created_num += 1

            attribute_list = magento.catalog_product_attribute.list(attribute_set.get('set_id'))

            for attribute in attribute_list:
                attribute_info = magento.catalog_product_attribute.info(attribute.get('attribute_id'))

                if check_attribute(attribute_info):
                    updated_values = {  'code': attribute.get('code'),
                                        'attribute_id': attribute.get('attribute_id'),
                                        'required': attribute.get('required'),
                                        'scope': attribute.get('scope'),
                                        'attribute_type': attribute.get('type'),
                                        'attribute_set': attribute_set_obj,
                                        'magento_attribute_set_id': attribute_set.get('set_id')
                                     }

                    attribute_obj, attribute_created = ProductAttribute.objects.update_or_create(
                                                        attribute_id=attribute.get('attribute_id'),
                                                        defaults=updated_values)
                    if attribute_created:
                        attribute_created_num += 1

    response_object = { 'sets_total': sets_total,
                        'sets_created_num': sets_created_num,
                        'attribute_created_num': attribute_created_num }
    return response_object




