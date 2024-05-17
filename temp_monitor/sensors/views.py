from django.shortcuts import render
from django.http import JsonResponse
from .models import TemperatureReading
from django.views.decorators.csrf import csrf_exempt
import json

#agregar codigo para insertar registros del sensor en base de datos
@csrf_exempt
def record_temperature(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        temperature = data['temperature']
        timestamp = data['timestamp']
        reading = TemperatureReading(temperature=temperature, timestamp=timestamp)
        reading.save()
        return JsonResponse({'status': 'success'})


def get_temperatures(request):
    readings = TemperatureReading.objects.all().order_by('-timestamp')
    data = [{'temperature': r.temperature, 'timestamp': r.timestamp} for r in readings]
    return JsonResponse(data, safe=False)
