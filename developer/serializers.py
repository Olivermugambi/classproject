# The serializer class prepares the json for the responses based on the developer model
from rest_framework import serializers

from .models import *

# the serializers for the developer and sprint models
class User_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ('email',)

class Developer_Serializer(serializers.HyperlinkedModelSerializer):
    user_details = User_Serializer()

    class Meta:
        model = Developer
        fields = ('developer_name', 'telephone', 'email', 'role', 'developer_status', 'user_details', 
        'registration_date')

    def create(self, validated_data):
        user, created = User.objects.get_or_create(email=validated_data.pop('user_details'))
        instance = Developer.objects.create(**validated_data, user_details=user)
        return instance

class Sprint_Serializer(serializers.HyperlinkedModelSerializer):
    added_by = Developer_Serializer()

    class Meta:
        model = Sprint()
        fields = ('start_date', 'end_date', 'expected_outcome', 'added_by')

class Sprint_Backlog_Serializer(serializers.HyperlinkedModelSerializer):
    sprint = Sprint_Serializer()
    added_by = Developer_Serializer()

    class Meta:
        model = Sprint_Backlog
        fields = ('sprint', 'backlog_item', 'added_by', 'creation_date', 'expected_outcome')

class Sprint_Backlog_Allocations_Serializer(serializers.HyperlinkedModelSerializer):
    sprint_backlog = Sprint_Backlog_Serializer()
    developer = Developer_Serializer()

    class Meta:
        model = Sprint_Backlog_Allocations
        fields = ('sprint_backlog', 'developer', 'creation_date', 'allocation_status')

class Daily_Scrum_Serializer(serializers.HyperlinkedModelSerializer):
    sprint_backlog = Sprint_Backlog_Serializer()

    class Meta:
        model = Daily_Scrum
        fields = ('date', 'sprint_backlog', 'outcome')

class Sprint_Review_Serializer(serializers.HyperlinkedModelSerializer):
    sprint = Sprint_Serializer()
    developer = Developer_Serializer()
    
    class Meta:
        model = Daily_Scrum
        fields = ('sprint', 'review', 'developer', 'creation_date', 'review_status')

class Sprint_Retrospective_Serializer(serializers.HyperlinkedModelSerializer):
    sprint = Sprint_Serializer()
    added_by = Developer_Serializer()
    
    class Meta:
        model = Sprint_Retrospective
        fields = ('sprint', 'added_by', 'retrospective', 'creation_date')