# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playtv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriado',
            name='titulo_ingles',
            field=models.CharField(default='nada_informado', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
