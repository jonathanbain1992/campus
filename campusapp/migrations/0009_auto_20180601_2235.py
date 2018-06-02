# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0008_auto_20180601_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='MenuItem',
        ),
        migrations.RemoveField(
            model_name='sideitem',
            name='foodItem',
        ),
        migrations.DeleteModel(
            name='FoodItem',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.DeleteModel(
            name='SideItem',
        ),
    ]
