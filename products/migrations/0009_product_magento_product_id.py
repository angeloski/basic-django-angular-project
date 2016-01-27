# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20150703_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='magento_product_id',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
    ]
