# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0018_auto_20180613_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='foodpurchases',
            field=models.ForeignKey(to='campusapp.FoodItem'),
        ),
    ]
