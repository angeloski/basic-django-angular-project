# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattribute',
            name='attribute_set',
            field=models.ForeignKey(to='products.AttributeSet', default=1),
            preserve_default=False,
        ),
    ]
