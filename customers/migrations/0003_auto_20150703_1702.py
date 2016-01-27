# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20150703_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='magento_customer_id',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='relation',
            name='magento_default_billing',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='relation',
            name='magento_default_shipping',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='relation',
            name='magento_group_id',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='relation',
            name='magento_store_id',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='relation',
            name='magento_website_id',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
