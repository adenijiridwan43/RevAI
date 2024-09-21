from django.db import models
# RevAi models here.



class SensorData(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    vibration = models.FloatField()

class MaintenanceEvent(models.Model):
    timestamp = models.DateTimeField()
    description = models.TextField()
