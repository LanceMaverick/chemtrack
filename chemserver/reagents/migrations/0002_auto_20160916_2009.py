# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liquidentry',
            old_name='reagent_number',
            new_name='reagent',
        ),
        migrations.RenameField(
            model_name='solidentry',
            old_name='reagent_number',
            new_name='reagent',
        ),
        migrations.RemoveField(
            model_name='liquidentry',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='solidentry',
            name='amount',
        ),
        migrations.AddField(
            model_name='solidentry',
            name='quantity',
            field=models.FloatField(null=True, verbose_name='amount used in (mg)'),
        ),
        migrations.AlterField(
            model_name='liquidentry',
            name='concentration',
            field=models.FloatField(null=True, verbose_name='concentration (%)'),
        ),
        migrations.AlterField(
            model_name='liquidentry',
            name='date',
            field=models.DateField(verbose_name='date of usage'),
        ),
        migrations.AlterField(
            model_name='liquidentry',
            name='volume',
            field=models.FloatField(null=True, verbose_name='quantity used (ml)'),
        ),
        migrations.AlterField(
            model_name='solidentry',
            name='date',
            field=models.DateField(verbose_name='date of usage'),
        ),
    ]
