# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-30 04:27
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('joinus', '0009_joinus_join_date'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='joinus',
            managers=[
                ('recipients', django.db.models.manager.Manager()),
            ],
        ),
    ]