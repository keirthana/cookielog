# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_dish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='id',
        ),
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
