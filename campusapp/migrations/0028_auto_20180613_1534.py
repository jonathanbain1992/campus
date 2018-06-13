# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0027_auto_20180613_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinkitem',
            name='Order',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='Order',
        ),
        migrations.AddField(
            model_name='order',
            name='DrinkItem',
            field=models.ForeignKey(default=None, to='campusapp.DrinkItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='FoodItem',
            field=models.ForeignKey(default=None, to='campusapp.FoodItem'),
        ),
    ]
