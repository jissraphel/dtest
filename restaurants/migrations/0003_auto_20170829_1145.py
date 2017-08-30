# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-29 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20170829_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]