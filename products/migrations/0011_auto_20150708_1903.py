# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20150706_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributeset',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 8, 19, 2, 57, 865767, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attributeset',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 8, 19, 3, 0, 901625, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='defaultonlineproperties',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 8, 19, 3, 2, 898150, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productattribute',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 8, 19, 3, 5, 81778, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productattribute',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 8, 19, 3, 6, 945615, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productdeliverytime',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 8, 19, 3, 8, 857160, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productdeliverytime',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 8, 19, 3, 10, 818315, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productonlineproperties',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 8, 19, 3, 12, 713548, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 8, 19, 3, 14, 625588, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 7, 8, 19, 3, 16, 177417, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
