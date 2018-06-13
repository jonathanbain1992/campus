# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0033_fooditem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='localDateTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 17, 28, 57, 756560)),
        ),
        migrations.AlterField(
            model_name='order',
            name='DrinkItem',
            field=models.ManyToManyField(default=None, to='campusapp.DrinkItem'),
        ),
        migrations.AlterField(
            model_name='order',
            name='FoodItem',
            field=models.ManyToManyField(default=None, to='campusapp.FoodItem'),
        ),
    ]
