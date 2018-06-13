# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0028_auto_20180613_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='DrinkItem',
        ),
        migrations.AddField(
            model_name='order',
            name='DrinkItem',
            field=models.ManyToManyField(default=None, to='campusapp.DrinkItem'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='FoodItem',
        ),
        migrations.AddField(
            model_name='order',
            name='FoodItem',
            field=models.ManyToManyField(default=None, to='campusapp.FoodItem'),
        ),
    ]
