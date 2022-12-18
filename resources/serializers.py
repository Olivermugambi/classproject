# The serializer class prepares the json for the responses based on the resources model
from rest_framework import serializers
from .models import *

# the serializers for the resources model
class Resource_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Resource
        fields = '__all__'

class Resource_Status_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Resource_Status
        fields = '__all__'

class Resource_Type_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Resource_Type
        fields = '__all__'

class Resource_Manager_Serializer(serializers.HyperlinkedModelSerializer):
    resources_managed = Resource_Serializer(many=True, read_only=True)

    class Meta:
        model = Resource_Manager
        fields = '__all__'