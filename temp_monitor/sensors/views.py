from django.shortcuts import render
from django.http import JsonResponse
from .models import TemperatureReading
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone


# agregar codigo para insertar registros del sensor en base de datos
@csrf_exempt
def potenciometro(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            sensor_name = data.get('sensor_name',
                                   'default_sensor')
            temperature = data['info']
            TemperatureReading.objects.create(sensor_name=sensor_name, temperature=temperature,
                                              timestamp=timezone.now())
            return JsonResponse({'message': 'Data received successfully'}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_temperatures(request):
    readings = TemperatureReading.objects.all().order_by('-timestamp')
    data = [{'temperature': r.temperature, 'timestamp': r.timestamp} for r in readings]
    return JsonResponse(data, safe=False)
