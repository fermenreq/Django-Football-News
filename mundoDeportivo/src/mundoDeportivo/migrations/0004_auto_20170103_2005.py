# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundoDeportivo', '0003_auto_20170103_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='noticia',
            field=models.TextField(max_length=9000),
        ),
    ]
