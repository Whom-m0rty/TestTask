from django.contrib import admin
from django.urls import path, include

from web.views import AddSensorReadings, ViewSensorReadingsAPI, ViewSensorReadingsTable

urlpatterns = [
    path('add/rf/', AddSensorReadings.as_view()),
    path('view/rf/', ViewSensorReadingsAPI.as_view()),
    path('view/table/', ViewSensorReadingsTable.as_view())
]