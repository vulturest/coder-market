# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-31 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder_market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='need_receiver_num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
