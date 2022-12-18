# The serializer class prepares the json for the responses based on the resources model
from rest_framework import serializers
from .models import *

# the serializers for the resources model
class Recommended_Adaptations_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Recommended_Adaptations
        fields = '__all__'

class Integration_Outcome_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Integration_Outcome
        fields = '__all__'

class Integration_Progress_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Integration_Progress
        fields = '__all__'

class Progress_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Progress
        fields = '__all__'

class Integration_Tool_Allocation_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Integration_Tool_Allocation
        fields = '__all__'

class Tool_Allocation_Status_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Tool_Allocation_Status
        fields = '__all__'

class Service_Integration_Tool_Serializer(serializers.HyperlinkedModelSerializer):
    integration_tool_allocations = Integration_Tool_Allocation_Serializer(many=True, read_only=True)
    
    class Meta:
        model = Service_Integration_Tool
        fields = '__all__'

class Integration_Tool_Type_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Integration_Tool_Type
        fields = '__all__'

class Integration_Tool_Status_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Integration_Tool_Status
        fields = '__all__'

class Service_Integration_Item_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Service_Integration_Item
        fields = '__all__'

class Service_Integrator_Serializer(serializers.HyperlinkedModelSerializer):
    service_integrator_recommended_adaptations = Recommended_Adaptations_Serializer(many=True, read_only=True)
    service_integration_outcomes = Integration_Outcome_Serializer(many=True, read_only=True)
    service_integrator_progress = Integration_Progress_Serializer(many=True, read_only=True)
    service_integrator_tool_allocations = Integration_Tool_Allocation_Serializer(many=True, read_only=True)
    service_integrator_items = Service_Integration_Item_Serializer(many=True, read_only=True)

    class Meta:
        model = Service_Integrator
        fields = '__all__'

class Service_Integration_Serializer(serializers.HyperlinkedModelSerializer):
    service_integration_items = Service_Integration_Item_Serializer(many=True, read_only=True)
    
    class Meta:
        model = Service_Integration
        fields = '__all__'

class Service_Integration_Status_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Service_Integration_Status
        fields = '__all__'

class Service_Pipeline_Item_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Service_Pipeline_Item
        fields = '__all__'

class Service_Type_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Service_Type
        fields = '__all__'

class Service_Pipeline_Item_Status_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Service_Pipeline_Item_Status
        fields = '__all__'

class Service_Pipeline_Serializer(serializers.HyperlinkedModelSerializer):
    service_pipeline_integration_items = Service_Integration_Item_Serializer(many=True, read_only=True)
    pipelined_items = Service_Pipeline_Item_Serializer(many=True, read_only=True)
    
    class Meta:
        model = Service_Pipeline
        fields = '__all__'