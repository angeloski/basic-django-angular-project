# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20150703_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='company',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='relation',
            name='name',
            field=models.CharField(max_length=60, blank=True, verbose_name='name', null=True),
        ),
        migrations.AlterField(
            model_name='relation',
            name='vat_number',
            field=models.CharField(max_length=100, blank=True, verbose_name='vat number', null=True),
        ),
    ]
