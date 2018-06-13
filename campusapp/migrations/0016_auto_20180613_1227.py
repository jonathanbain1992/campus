# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('campusapp', '0015_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='drinkspurchases',
            field=models.ForeignKey(related_name='DrinkItem', default=b'', to='campusapp.DrinkItem'),
        ),
        migrations.AddField(
            model_name='customer',
            name='foodpurchases',
            field=models.ForeignKey(related_name='FoodItem', default=b'', to='campusapp.FoodItem'),
        ),
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(default=None, upload_to=b''),
        ),
        migrations.AddField(
            model_name='customer',
            name='niftyfiftypts',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tel_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(related_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]
