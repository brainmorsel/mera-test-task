# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverheartbeat',
            name='server_fqdn',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='serverheartbeat',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
