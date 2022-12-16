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

class Developer_Name_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Developer
        fields = ('developer_name', )

class Sprint_Serializer(serializers.HyperlinkedModelSerializer):
    added_by = Developer_Name_Serializer()

    class Meta:
        model = Sprint()
        fields = ('start_date', 'end_date', 'expected_outcome', 'added_by')
    
    def create(self, validated_data):
        added_by, created = Developer.objects.get_or_create(developer_name=validated_data.pop('added_by'))
        instance = Sprint.objects.create(**validated_data, added_by=added_by)
        return instance

class Sprint_Field_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Sprint()
        fields = ( 'expected_outcome', )

class Sprint_Backlog_Serializer(serializers.HyperlinkedModelSerializer):
    sprint = Sprint_Field_Serializer()
    added_by = Developer_Name_Serializer()

    class Meta:
        model = Sprint_Backlog
        fields = ('sprint', 'backlog_item', 'added_by', 'creation_date', 'expected_outcome')

    def create(self, validated_data):
        sprint, created = Sprint.objects.get_or_create(expected_outcome=validated_data.pop('sprint'))
        added_by, created = Developer.objects.get_or_create(developer_name=validated_data.pop('added_by'))
        instance = Sprint_Backlog.objects.create(**validated_data, added_by=added_by, sprint=sprint)
        return instance

class Sprint_Backlog_Field_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Sprint_Backlog()
        fields = ( 'backlog_item', )

class Sprint_Backlog_Allocations_Serializer(serializers.HyperlinkedModelSerializer):
    sprint_backlog = Sprint_Backlog_Field_Serializer()
    developer = Developer_Name_Serializer()

    class Meta:
        model = Sprint_Backlog_Allocations
        fields = ('sprint_backlog', 'developer', 'creation_date', 'allocation_status')

    def create(self, validated_data):
        sprint_backlog, created = Sprint_Backlog.objects.get_or_create(backlog_item=validated_data.pop('sprint_backlog'))
        developer, created = Developer.objects.get_or_create(developer_name=validated_data.pop('developer'))
        instance = Sprint_Backlog_Allocations.objects.create(**validated_data, developer=developer, sprint_backlog=sprint_backlog)
        return instance

class Daily_Scrum_Serializer(serializers.HyperlinkedModelSerializer):
    sprint_backlog = Sprint_Backlog_Field_Serializer()

    class Meta:
        model = Daily_Scrum
        fields = ('date', 'sprint_backlog', 'outcome')

    def create(self, validated_data):
        sprint_backlog, created = Sprint_Backlog.objects.get_or_create(backlog_item=validated_data.pop('sprint_backlog'))
        instance = Daily_Scrum.objects.create(**validated_data, sprint_backlog=sprint_backlog)
        return instance

class Sprint_Review_Serializer(serializers.HyperlinkedModelSerializer):
    sprint = Sprint_Field_Serializer()
    developer = Developer_Name_Serializer()
    
    class Meta:
        model = Sprint_Review
        fields = ('sprint', 'review', 'developer', 'creation_date', 'review_status')

    def create(self, validated_data):
        sprint, created = Sprint.objects.get_or_create(expected_outcome=validated_data.pop('sprint'))
        developer, created = Developer.objects.get_or_create(developer_name=validated_data.pop('developer'))
        instance = Sprint_Review.objects.create(**validated_data, sprint=sprint, developer=developer)
        return instance

class Sprint_Retrospective_Serializer(serializers.HyperlinkedModelSerializer):
    sprint = Sprint_Field_Serializer()
    added_by = Developer_Name_Serializer()
    
    class Meta:
        model = Sprint_Retrospective
        fields = ('sprint', 'added_by', 'retrospective', 'creation_date')

    def create(self, validated_data):
        sprint, created = Sprint.objects.get_or_create(expected_outcome=validated_data.pop('sprint'))
        added_by, created = Developer.objects.get_or_create(developer_name=validated_data.pop('added_by'))
        instance = Sprint_Review.objects.create(**validated_data, sprint=sprint, added_by=added_by)
        return instance