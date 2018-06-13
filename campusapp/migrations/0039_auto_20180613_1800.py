# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0038_auto_20180613_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkitem',
            name='Order',
            field=models.ManyToManyField(to='campusapp.Order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='localDateTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 18, 0, 52, 541515), editable=False),
        ),
    ]
