# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 06:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170729_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='MQTT',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Device')),
                ('mqtt_type', models.CharField(choices=[('mqtt', 'MQTT'), ('mqtt-sn', 'MQTT-SN')], default='mqtt', max_length=10, verbose_name='Видпротокола')),
                ('role', models.CharField(choices=[('publisher', 'Publisher'), ('consumer', 'Consumer')], default='slave', max_length=10, verbose_name='Роль устройства')),
            ],
            options={
                'verbose_name': 'Устройство MQTT',
                'verbose_name_plural': 'Устройства MQTT',
            },
            bases=('main.device',),
        ),
        migrations.AddField(
            model_name='modbus',
            name='modbus_type',
            field=models.CharField(choices=[('tcp', 'TCP'), ('ascii', 'ASCII'), ('rtu', 'RTU')], default='tcp', max_length=10, verbose_name='Вид протокола'),
        ),
    ]
