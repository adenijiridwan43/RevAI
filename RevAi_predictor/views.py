from rest_framework import viewsets
from .models import SensorData, MaintenanceEvent
from rest_framework.response import Response
from .serializers import SensorDataSerializer, MaintenanceEventSerializer
from .data_processing import clean_and_preprocess_data


# views

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data
        if isinstance(data, list):
            cleaned_data = clean_and_preprocess_data(data)
        else:
            cleaned_data = clean_and_preprocess_data([data])[0]
        
        serializer = self.get_serializer(data=cleaned_data, many=isinstance(cleaned_data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

class MaintenanceEventViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceEvent.objects.all()
    serializer_class = MaintenanceEventSerializer