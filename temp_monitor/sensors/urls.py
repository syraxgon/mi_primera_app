from django.urls import path
from .views import potenciometro, get_temperatures

urlpatterns = [
    path('record/', potenciometro, name='record_temperature'),
    path('temperatures/', get_temperatures, name='get_temperatures'),
]