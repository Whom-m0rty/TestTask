from rest_framework import serializers

from web.models import SensorReadings


class SensorReadingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorReadings
        fields = ['sensor_type', 'num', 'name', 'temperature', 'humidity']
