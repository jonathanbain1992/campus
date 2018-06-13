# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0023_item_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='itemType',
            field=models.CharField(default=0, max_length=10, choices=[(0, b'food'), (1, b'drink')]),
        ),
    ]
