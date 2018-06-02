# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0005_auto_20180526_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200)),
                ('price', models.FloatField(default=0.0)),
                ('image', models.ImageField(default=None, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200)),
                ('valid_from', models.DateTimeField()),
                ('valid_until', models.DateTimeField()),
                ('image', models.ImageField(default=None, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='SideItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('Quantity', models.IntegerField(default=0)),
                ('image', models.ImageField(default=None, upload_to=b'')),
                ('foodItem', models.ForeignKey(to='campusapp.FoodItem')),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default=None, upload_to=b''),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='MenuItem',
            field=models.OneToOneField(to='campusapp.MenuItem'),
        ),
    ]
