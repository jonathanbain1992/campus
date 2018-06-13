# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0026_auto_20180613_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderCreationDateTime',
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='Item',
            field=models.OneToOneField(related_name='Item', to='campusapp.Item'),
        ),
    ]
