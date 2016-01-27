# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='postalcode',
        ),
        migrations.AddField(
            model_name='address',
            name='country_id',
            field=models.CharField(null=True, max_length=5, blank=True),
        ),
        migrations.AddField(
            model_name='address',
            name='magento_customer_address_id',
            field=models.CharField(null=True, max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='address',
            name='magento_is_default_billing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='address',
            name='magento_is_default_shipping',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='address',
            name='magento_region_id',
            field=models.CharField(null=True, max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='address',
            name='postcode',
            field=models.CharField(null=True, max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='address',
            name='region',
            field=models.CharField(null=True, max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(null=True, max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(null=True, max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_1',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_2',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_3',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(null=True, max_length=150, blank=True),
        ),
    ]
