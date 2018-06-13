# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0039_auto_20180613_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinkitem',
            name='Order',
        ),
        migrations.AlterField(
            model_name='order',
            name='localDateTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 18, 1, 48, 66263), editable=False),
        ),
    ]
