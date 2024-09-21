from rest_framework import viewsets
from .models import SensorData, MaintenanceEvent
from .serializers import SensorDataSerializer, MaintenanceEventSerializer


# views

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer

class MaintenanceEventViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceEvent.objects.all()
    serializer_class = MaintenanceEventSerializer