# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('set_id', models.CharField(null=True, max_length=10, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('product_type', models.CharField(choices=[('simple', 'Simple'), ('configurable', 'Configurable'), ('grouped', 'Grouped'), ('bundle', 'Bundle'), ('virtual', 'Virtual'), ('downloadable', 'Downloadable')], max_length=30, default='configurable')),
                ('stock', models.PositiveIntegerField(null=True, blank=True)),
                ('minimum_order_quantity', models.PositiveIntegerField(null=True, blank=True)),
                ('sku', models.CharField(null=True, verbose_name='SKU', max_length=120, blank=True)),
                ('name', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attribute_set', models.ForeignKey(null=True, blank=True, to='products.AttributeSet')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=100)),
                ('attribute_id', models.CharField(null=True, max_length=10, blank=True)),
                ('required', models.BooleanField()),
                ('scope', models.CharField(null=True, max_length=20, blank=True)),
                ('attribute_type', models.CharField(null=True, max_length=20, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDeliveryTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('days', models.PositiveIntegerField()),
                ('verbose_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOnlineProperties',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('available_on_website', models.BooleanField(default=False)),
                ('purchable_from_website', models.BooleanField(default=False)),
                ('name', models.CharField(null=True, max_length=120, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('advantage_1', models.CharField(null=True, max_length=120, blank=True)),
                ('advantage_2', models.CharField(null=True, max_length=120, blank=True)),
                ('advantage_3', models.CharField(null=True, max_length=120, blank=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
                'verbose_name_plural': 'Product online properties',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('code', models.CharField(max_length=100)),
                ('is_active', models.BooleanField()),
                ('group_id', models.CharField(max_length=100)),
                ('sort_order', models.CharField(max_length=100)),
                ('store_id', models.CharField(max_length=100)),
                ('website_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='productonlineproperties',
            name='store',
            field=models.ForeignKey(to='products.Store'),
        ),
        migrations.AddField(
            model_name='product',
            name='delivery_time',
            field=models.ForeignKey(null=True, blank=True, to='products.ProductDeliveryTime'),
        ),
        migrations.AddField(
            model_name='product',
            name='products_associated_with',
            field=models.ManyToManyField(to='products.Product', related_name='products_associated_with_rel_+', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(to='customers.Relation'),
        ),
        migrations.AlterUniqueTogether(
            name='productonlineproperties',
            unique_together=set([('store', 'product')]),
        ),
    ]
