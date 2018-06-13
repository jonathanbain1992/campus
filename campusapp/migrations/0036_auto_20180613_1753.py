# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0035_auto_20180613_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='DrinkItem',
        ),
        migrations.AddField(
            model_name='order',
            name='DrinkItem',
            field=models.ForeignKey(default=None, to='campusapp.DrinkItem'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='FoodItem',
        ),
        migrations.AddField(
            model_name='order',
            name='FoodItem',
            field=models.ForeignKey(default=None, to='campusapp.FoodItem'),
        ),
        migrations.AlterField(
            model_name='order',
            name='localDateTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 17, 53, 12, 544255), editable=False),
        ),
    ]
