# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_model', '0004_auto_20170720_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slowquery',
            name='comments',
            field=models.TextField(null=True),
        ),
    ]