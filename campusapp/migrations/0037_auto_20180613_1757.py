# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0036_auto_20180613_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='DrinkItem',
        ),
        migrations.RemoveField(
            model_name='order',
            name='FoodItem',
        ),
        migrations.AddField(
            model_name='drinkitem',
            name='Order',
            field=models.ForeignKey(default=None, to='campusapp.Order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='localDateTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 17, 57, 22, 971175), editable=False),
        ),
    ]
