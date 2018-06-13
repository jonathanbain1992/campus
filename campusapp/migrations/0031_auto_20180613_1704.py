# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0030_auto_20180613_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinkitem',
            name='Item',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='Item',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
