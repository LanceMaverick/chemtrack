# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 23:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0003_auto_20160918_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reagent',
            name='cid',
        ),
    ]
