# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-18 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.IntegerField(default=0)),
                ('direction', models.CharField(max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='WindSpeed',
        ),
    ]
