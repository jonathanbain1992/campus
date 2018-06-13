# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0034_auto_20180613_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='localDateTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 17, 29, 50, 950198)),
        ),
    ]
