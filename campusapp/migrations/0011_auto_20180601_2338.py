# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0010_item_sideitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Item', models.ForeignKey(to='campusapp.Item')),
            ],
        ),
        migrations.RemoveField(
            model_name='sideitem',
            name='Item',
        ),
        migrations.DeleteModel(
            name='SideItem',
        ),
    ]
