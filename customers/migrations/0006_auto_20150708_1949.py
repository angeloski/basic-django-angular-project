# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20150708_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='relation',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='relation',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
