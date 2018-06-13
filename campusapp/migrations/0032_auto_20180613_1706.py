# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0031_auto_20180613_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinkitem',
            name='description',
            field=models.TextField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='drinkitem',
            name='image',
            field=models.ImageField(default=None, upload_to=b''),
        ),
        migrations.AddField(
            model_name='drinkitem',
            name='name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='drinkitem',
            name='price',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='description',
            field=models.TextField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='image',
            field=models.ImageField(default=None, upload_to=b''),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='price',
            field=models.FloatField(default=None),
        ),
    ]
