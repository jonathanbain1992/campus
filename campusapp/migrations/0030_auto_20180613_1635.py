# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0029_auto_20180613_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='Item',
            field=models.OneToOneField(to='campusapp.Item'),
        ),
        migrations.AlterField(
            model_name='order',
            name='DrinkItem',
            field=models.ManyToManyField(to='campusapp.DrinkItem'),
        ),
        migrations.AlterField(
            model_name='order',
            name='FoodItem',
            field=models.ManyToManyField(to='campusapp.FoodItem'),
        ),
    ]
