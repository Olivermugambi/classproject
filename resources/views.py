from rest_framework import viewsets
from .serializers import *


class Resource_ViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all().order_by('acquisition_date')
    serializer_class = Resource_Serializer

class Resource_Status_ViewSet(viewsets.ModelViewSet):
    queryset = Resource_Status.objects.all().order_by('resource_status')
    serializer_class = Resource_Status_Serializer

class Resource_Type_ViewSet(viewsets.ModelViewSet):
    queryset = Resource_Type.objects.all().order_by('resource_type')
    serializer_class = Resource_Type_Serializer

class Resource_Manager_ViewSet(viewsets.ModelViewSet):
    queryset = Resource_Manager.objects.all().order_by('created_on')
    serializer_class = Resource_Manager_Serializer