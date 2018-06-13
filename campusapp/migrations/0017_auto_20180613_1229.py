# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0016_auto_20180613_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='tel_no',
            field=models.IntegerField(default=0),
        ),
    ]
