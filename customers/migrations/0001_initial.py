# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('line_1', models.CharField(max_length=300, blank=True)),
                ('line_2', models.CharField(max_length=300, blank=True)),
                ('line_3', models.CharField(max_length=300, blank=True)),
                ('city', models.CharField(max_length=150, blank=True)),
                ('postalcode', models.CharField(max_length=10, blank=True)),
                ('state', models.CharField(max_length=150, blank=True)),
                ('country', models.CharField(max_length=150, blank=True)),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('is_client', models.BooleanField(verbose_name='is client', default=False)),
                ('is_supplier', models.BooleanField(verbose_name='is supplier', default=False)),
                ('name', models.CharField(verbose_name='name', max_length=60)),
                ('company', models.CharField(max_length=100, blank=True)),
                ('phone_number', models.CharField(null=True, max_length=30, blank=True)),
                ('email', models.EmailField(null=True, verbose_name='email address', max_length=255, blank=True)),
                ('is_active', models.BooleanField(verbose_name='active', default=True)),
                ('vat_number', models.CharField(verbose_name='vat number', max_length=100, blank=True)),
                ('sku', models.CharField(null=True, verbose_name='SKU', max_length=120, blank=True)),
                ('addresses', models.ManyToManyField(to='customers.Address', blank=True)),
            ],
        ),
    ]
