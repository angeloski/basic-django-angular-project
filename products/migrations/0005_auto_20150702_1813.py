# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20150702_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorytree',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 18, 13, 8, 927459, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categorytree',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 18, 13, 15, 376662, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
