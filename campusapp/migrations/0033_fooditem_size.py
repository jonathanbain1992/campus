# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0032_auto_20180613_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='size',
            field=models.IntegerField(default=0, choices=[(0, b'small'), (0, b'medium'), (0, b'large')]),
        ),
    ]
