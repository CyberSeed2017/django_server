# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-01 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20171001_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Record_ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]