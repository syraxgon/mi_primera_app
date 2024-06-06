from django.db import models
from django.utils import timezone


# Create your models here.
class TemperatureReading(models.Model):
    sensor_name = models.CharField(max_length=100)
    temperature = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.temperature} at {self.timestamp}"
