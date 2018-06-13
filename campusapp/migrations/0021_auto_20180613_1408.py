# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0020_auto_20180613_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkitem',
            name='Customer',
            field=models.ForeignKey(to='campusapp.Customer'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='Customer',
            field=models.ForeignKey(to='campusapp.Customer'),
        ),
    ]
