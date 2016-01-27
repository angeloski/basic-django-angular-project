# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productattribute_magento_attribute_set_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('category_tree', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
