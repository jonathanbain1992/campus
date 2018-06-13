# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0019_auto_20180613_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='drinkspurchases',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='foodpurchases',
        ),
        migrations.AddField(
            model_name='drinkitem',
            name='Customer',
            field=models.ForeignKey(default=None, to='campusapp.Customer'),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='Customer',
            field=models.ForeignKey(default=None, to='campusapp.Customer'),
        ),
        migrations.AlterField(
            model_name='drinkitem',
            name='Quantity',
            field=models.IntegerField(default=0, choices=[(330, b'330ml'), (660, b'660ml'), (284, b'half pint'), (568, b'pint'), (1136, b'2 pint pitcher')]),
        ),
    ]
