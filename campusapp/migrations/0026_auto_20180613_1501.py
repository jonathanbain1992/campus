# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0025_auto_20180613_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='drinkItems',
        ),
        migrations.RemoveField(
            model_name='order',
            name='foodItems',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.AddField(
            model_name='drinkitem',
            name='Order',
            field=models.ForeignKey(default=None, to='campusapp.Order'),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='Order',
            field=models.ForeignKey(default=None, to='campusapp.Order'),
        ),
    ]
