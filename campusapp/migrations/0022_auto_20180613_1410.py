# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0021_auto_20180613_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinkitem',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='Customer',
        ),
    ]
