# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_auto_20170816_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='positions.Position'),
        ),
    ]
