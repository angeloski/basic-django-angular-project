# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productattribute_attribute_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattribute',
            name='magento_attribute_set_id',
            field=models.CharField(null=True, blank=True, max_length=20),
        ),
    ]
