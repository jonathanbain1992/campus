# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0007_auto_20180601_0259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='description',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='name',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='price',
        ),
    ]
