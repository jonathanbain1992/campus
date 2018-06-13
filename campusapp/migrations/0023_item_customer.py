# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0022_auto_20180613_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='customer',
            field=models.ForeignKey(default=None, to='campusapp.Customer'),
        ),
    ]
