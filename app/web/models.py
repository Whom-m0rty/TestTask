from django.db import models


# Create your models here.

class SensorType(models.IntegerChoices):
    DEFAULT = 0, 'Стандартный'
    WATER = 1, 'Воды'
    FIRE = 2, 'Огня'
    SMOKE = 4, 'Влажности'
    SUN = 10, 'Температуры'


class SensorReadings(models.Model):
    class Meta:
        verbose_name = 'Показатели датчика'
        verbose_name_plural = 'Показатель датчика'
        db_table = 'sensor_readings'

    sensor_type = models.IntegerField(choices=SensorType.choices, verbose_name='Тип датчика')
    num = models.IntegerField(primary_key=True, unique=True, verbose_name='Порядковый номер')
    name = models.TextField(default='N/A', null=True, blank=True, verbose_name='Имя датчика')
    temperature = models.IntegerField(null=True, blank=True, verbose_name='Температура')
    humidity = models.IntegerField(blank=True, null=True, verbose_name='Влажность')

