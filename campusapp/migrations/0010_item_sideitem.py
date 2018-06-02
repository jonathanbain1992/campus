# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0009_auto_20180601_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200)),
                ('price', models.FloatField(default=0.0)),
                ('image', models.ImageField(default=None, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='SideItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField(default=0.0)),
                ('description', models.TextField(max_length=200)),
                ('image', models.ImageField(default=None, upload_to=b'')),
                ('Item', models.ForeignKey(to='campusapp.Item')),
            ],
        ),
    ]
