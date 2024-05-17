from django.urls import path
from .views import record_temperature, get_temperatures

urlpatterns = [
    path('record/', record_temperature, name='record_temperature'),
    path('temperatures/', get_temperatures, name='get_temperatures'),
]