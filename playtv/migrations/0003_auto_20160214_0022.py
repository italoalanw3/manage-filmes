# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playtv', '0002_seriado_titulo_ingles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Execucao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco_ip', models.CharField(max_length=100)),
                ('nome_maquina', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Em execucao',
                'verbose_name_plural': 'Em execucao',
            },
        ),
        migrations.DeleteModel(
            name='Play',
        ),
        migrations.AddField(
            model_name='linksepisodioseriado',
            name='peers',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='linksepisodioseriado',
            name='seeds',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='linksepisodioseriado',
            name='torrent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='linksfilme',
            name='peers',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='linksfilme',
            name='seeds',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='linksfilme',
            name='torrent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='linksepisodioseriado',
            name='link',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='linksfilme',
            name='link',
            field=models.TextField(),
        ),
    ]
