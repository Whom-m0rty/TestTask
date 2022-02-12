from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from rest_framework import generics

# Create your views here.
from rest_framework.response import Response

from web.models import SensorReadings
from web.serializers import SensorReadingsSerializer
from web.utils import get_all_sensor_readings


class AddSensorReadings(generics.ListCreateAPIView):
    serializer_class = SensorReadingsSerializer
    queryset = SensorReadings.objects.all()

    def create(self, request, *args, **kwargs):
        # Перевод из  Sensor_type в sensor_type
        for d in request.data:
            d['sensor_type'] = d.pop('Sensor_type')

        # Для того, что бы serializer принимал list значений
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)


class ViewSensorReadingsAPI(generics.ListAPIView):
    serializer_class = SensorReadingsSerializer
    queryset = SensorReadings.objects.all()


class ViewSensorReadingsTable(View):
    def get(self, request):
        print(get_all_sensor_readings())
        return render(request, 'index.html', context={'data': get_all_sensor_readings()})
