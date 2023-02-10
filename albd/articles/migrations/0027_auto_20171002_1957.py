# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-02 13:57
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations
import albd.articles.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0026_auto_20171002_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=albd.articles.models.unique_slug_generator),
        ),
    ]