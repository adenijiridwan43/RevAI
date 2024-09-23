from django.db import models
# RevAi models here.



class SensorData(models.Model):
    device_id = models.CharField(max_length=100)
    pressure = models.FloatField()
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    vibration = models.FloatField()
    
    def __str__(self):
        return f"{self.device_id} - {self.timestamp}"

class MaintenanceEvent(models.Model):
    timestamp = models.DateTimeField()
    description = models.TextField()
