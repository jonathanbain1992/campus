# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0024_item_itemtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.IntegerField(default=472.5, editable=False)),
                ('orderCreationDateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='item',
            name='itemType',
        ),
        migrations.AlterField(
            model_name='drinkitem',
            name='Item',
            field=models.OneToOneField(to='campusapp.Item'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='Item',
            field=models.OneToOneField(to='campusapp.Item'),
        ),
        migrations.AddField(
            model_name='order',
            name='drinkItems',
            field=models.ForeignKey(to='campusapp.DrinkItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='foodItems',
            field=models.ForeignKey(to='campusapp.FoodItem'),
        ),
    ]
