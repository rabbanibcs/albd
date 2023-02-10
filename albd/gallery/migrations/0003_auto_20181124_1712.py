# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-24 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20171221_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryitem',
            name='source',
            field=models.CharField(choices=[('youtube', 'Youtube'), ('vimeo', 'Vimeo'), ('local', 'Local'), ('facebook', 'Facebook')], max_length=10),
        ),
    ]
