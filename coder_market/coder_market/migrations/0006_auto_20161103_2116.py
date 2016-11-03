# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-03 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder_market', '0005_remove_project_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='accept_information',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='manage_project',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_manager',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_receiver',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='accept_information',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='order_project',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='receiver',
            name='accept_information',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='receiver',
            name='get_project',
            field=models.IntegerField(null=True),
        ),
    ]
