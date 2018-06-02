# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0012_drinkitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinkitem',
            name='Quantity',
            field=models.CharField(default=b'', max_length=20, choices=[(330, b'330ml'), (660, b'660ml'), (284, b'half pint'), (568, b'pint'), (1136, b'2 pint pitcher')]),
        ),
    ]
