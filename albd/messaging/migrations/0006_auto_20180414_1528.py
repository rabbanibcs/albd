# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-14 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20180414_1528'),
        ('messaging', '0005_auto_20180407_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.Designation'),
        ),
        migrations.AddField(
            model_name='email',
            name='include_contacts',
            field=models.BooleanField(default=False, verbose_name='Include Contacts'),
        ),
        migrations.AddField(
            model_name='message',
            name='designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.Designation'),
        ),
        migrations.AddField(
            model_name='message',
            name='include_contacts',
            field=models.BooleanField(default=False, verbose_name='Include Contacts'),
        ),
    ]