from rest_framework import viewsets
from .serializers import *


class Service_Pipeline_ViewSet(viewsets.ModelViewSet):
    queryset = Service_Pipeline.objects.all().order_by('name')
    serializer_class = Service_Pipeline_Serializer

class Service_Pipeline_Item_Status_ViewSet(viewsets.ModelViewSet):
    queryset = Service_Pipeline_Item_Status.objects.all().order_by('status')
    serializer_class = Service_Pipeline_Item_Status_Serializer

class Service_Type_ViewSet(viewsets.ModelViewSet):
    queryset = Service_Type.objects.all().order_by('type')
    serializer_class = Service_Type_Serializer

class Service_Pipeline_Item_ViewSet(viewsets.ModelViewSet):
    queryset = Service_Pipeline_Item.objects.all().order_by('service')
    serializer_class = Service_Pipeline_Item_Serializer

class Service_Integration_Status_ViewSet(viewsets.ModelViewSet):
    queryset = Service_Integration_Status.objects.all().order_by('status')
    serializer_class = Service_Integration_Status_Serializer

class Service_Integration_ViewSet(viewsets.ModelViewSet):
    queryset = Service_Integration.objects.all().order_by('name')
    serializer_class = Service_Integration_Serializer

class Service_Integrator_ViewSet(viewsets.ModelViewSet):
    queryset = Service_Integrator.objects.all().order_by('name')
    serializer_class = Service_Integrator_Serializer

class Service_Integration_Item_ViewSet(viewsets.ModelViewSet):
    queryset = Service_Integration_Item.objects.all().order_by('creation_date')
    serializer_class = Service_Integration_Item_Serializer

class Integration_Tool_Status_ViewSet(viewsets.ModelViewSet):
    queryset = Integration_Tool_Status.objects.all().order_by('status')
    serializer_class = Integration_Tool_Status_Serializer

class Integration_Tool_Type_ViewSet(viewsets.ModelViewSet):
    queryset = Integration_Tool_Type.objects.all().order_by('type')
    serializer_class = Integration_Tool_Type_Serializer

class Service_Integration_Tool_ViewSet(viewsets.ModelViewSet):
    queryset = Service_Integration_Tool.objects.all().order_by('creation_date')
    serializer_class = Service_Integration_Tool_Serializer

class Tool_Allocation_Status_ViewSet(viewsets.ModelViewSet):
    queryset = Tool_Allocation_Status.objects.all().order_by('status')
    serializer_class = Tool_Allocation_Status_Serializer

class Integration_Tool_Allocation_ViewSet(viewsets.ModelViewSet):
    queryset = Integration_Tool_Allocation.objects.all().order_by('allocation_date')
    serializer_class = Integration_Tool_Allocation_Serializer

class Progress_ViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all().order_by('progress')
    serializer_class = Progress_Serializer

class Integration_Progress_ViewSet(viewsets.ModelViewSet):
    queryset = Integration_Progress.objects.all().order_by('checkpoint_date')
    serializer_class = Integration_Progress_Serializer

class Integration_Outcome_ViewSet(viewsets.ModelViewSet):
    queryset = Integration_Outcome.objects.all().order_by('outcome')
    serializer_class = Integration_Outcome_Serializer

class Recommended_Adaptations_ViewSet(viewsets.ModelViewSet):
    queryset = Recommended_Adaptations.objects.all().order_by('recommendation')
    serializer_class = Recommended_Adaptations_Serializer