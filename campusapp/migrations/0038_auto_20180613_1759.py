# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0037_auto_20180613_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinkitem',
            name='Order',
        ),
        migrations.AddField(
            model_name='drinkitem',
            name='Order',
            field=models.ManyToManyField(default=None, to='campusapp.Order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='localDateTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 17, 59, 51, 157572), editable=False),
        ),
    ]
