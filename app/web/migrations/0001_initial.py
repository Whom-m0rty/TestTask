# Generated by Django 4.0.2 on 2022-02-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorReadings',
            fields=[
                ('sensor_type', models.IntegerField(choices=[(0, 'Стандартный'), (1, 'Воды'), (2, 'Огня'), (4, 'Влажности'), (10, 'Температуры')], verbose_name='Тип датчика')),
                ('num', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Порядковый номер')),
                ('name', models.TextField(blank=True, default='N/A', null=True, verbose_name='Имя датчика')),
                ('temperature', models.IntegerField(blank=True, null=True, verbose_name='Температура')),
                ('humidity', models.IntegerField(blank=True, null=True, verbose_name='Влажность')),
            ],
            options={
                'verbose_name': 'Показатели датчика',
                'verbose_name_plural': 'Показатель датчика',
                'db_table': 'sensor_readings',
            },
        ),
    ]
