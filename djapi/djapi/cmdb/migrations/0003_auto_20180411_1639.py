# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-04-11 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20180411_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='host_env',
            field=models.CharField(max_length=30, null=True, verbose_name='\u8fd0\u884c\u73af\u5883'),
        ),
    ]