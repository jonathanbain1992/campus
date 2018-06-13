# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0017_auto_20180613_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='drinkspurchases',
            field=models.ForeignKey(to='campusapp.DrinkItem'),
        ),
    ]
