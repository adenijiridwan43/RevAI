from rest_framework import serializers
from .models import SensorData, MaintenanceEvent

class SensorDataSerializer(serializers.ModelSerializer):
     class Meta:
        model = SensorData
        fields = ['id', 'device_id', 'timestamp', 'temperature', 'pressure', 'vibration']


class MaintenanceEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceEvent
        fields = '__all__'