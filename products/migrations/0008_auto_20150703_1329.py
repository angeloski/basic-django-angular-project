# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20150703_1327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='defaultonlineproperties',
            options={'verbose_name_plural': 'Default product online properties'},
        ),
        migrations.AddField(
            model_name='defaultonlineproperties',
            name='product',
            field=models.ForeignKey(to='products.Product', default=1),
            preserve_default=False,
        ),
    ]
