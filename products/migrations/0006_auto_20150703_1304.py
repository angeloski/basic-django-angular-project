# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20150702_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultOnlineProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('available_on_website', models.BooleanField(default=False)),
                ('purchable_from_website', models.BooleanField(default=False)),
                ('name', models.CharField(null=True, max_length=120, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('advantage_1', models.CharField(null=True, max_length=120, blank=True)),
                ('advantage_2', models.CharField(null=True, max_length=120, blank=True)),
                ('advantage_3', models.CharField(null=True, max_length=120, blank=True)),
                ('product', models.ForeignKey(to='products.Product')),
                ('store', models.ForeignKey(to='products.Store')),
            ],
            options={
                'verbose_name_plural': 'Product online properties',
            },
        ),
        migrations.AlterUniqueTogether(
            name='defaultonlineproperties',
            unique_together=set([('store', 'product')]),
        ),
    ]
