# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-01 23:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_auto_20171001_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_Exam_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now=True, verbose_name='Date of exam')),
                ('Notes', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('Doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Doctor_conducted_exam', to=settings.AUTH_USER_MODEL)),
                ('Record', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Record')),
            ],
        ),
    ]