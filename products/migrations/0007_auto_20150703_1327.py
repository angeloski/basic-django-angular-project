# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150703_1304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='defaultonlineproperties',
            options={'verbose_name_plural': 'Default online properties'},
        ),
        migrations.AlterUniqueTogether(
            name='defaultonlineproperties',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='defaultonlineproperties',
            name='product',
        ),
        migrations.RemoveField(
            model_name='defaultonlineproperties',
            name='store',
        ),
    ]
