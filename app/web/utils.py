from web.models import SensorReadings


def get_all_sensor_readings():
    return SensorReadings.objects.all()