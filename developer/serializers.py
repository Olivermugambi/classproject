# The serializer class prepares the json for the responses based on the developer model
from rest_framework import serializers
from .models import *
from scrummaster.serializers import *
from resources.serializers import Resource_Manager_Serializer
from serviceintegrator.serializers import *

# the serializers for the developer and sprint models
class Sprint_Review_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Sprint_Review
        fields = '__all__'

class Sprint_Retrospective_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Sprint_Retrospective
        fields = '__all__'

class Daily_Scrum_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Daily_Scrum
        fields = '__all__'

class Sprint_Backlog_Allocations_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Sprint_Backlog_Allocations
        fields = '__all__'

class Sprint_Backlog_Serializer(serializers.HyperlinkedModelSerializer):
    sprint_backlog_allocations = Sprint_Backlog_Allocations_Serializer(many=True, read_only=True)
    
    class Meta:
        model = Sprint_Backlog
        fields = '__all__'

class Sprint_Serializer(serializers.HyperlinkedModelSerializer):
    sprint_backlogs = Sprint_Backlog_Serializer(many=True, read_only=True)
    sprint_daily_scrums = Daily_Scrum_Serializer(many=True, read_only=True)
    sprint_reviews = Sprint_Review_Serializer(many=True, read_only=True)
    sprint_retrospectives = Sprint_Retrospective_Serializer(many=True, read_only=True)

    class Meta:
        model = Sprint
        fields = '__all__'

class Developer_Serializer(serializers.ModelSerializer):
    developer_sprints = Sprint_Serializer(many=True, read_only=True)
    developer_sprint_backlogs = Sprint_Backlog_Serializer(many=True, read_only=True)
    developer_sprint_backlog_allocations = Sprint_Backlog_Allocations_Serializer(many=True, read_only=True)
    developer_daily_scrums = Daily_Scrum_Serializer(many=True, read_only=True)
    developer_sprint_reviews = Sprint_Review_Serializer(many=True, read_only=True)
    developer_sprint_retrospectives = Sprint_Retrospective_Serializer(many=True, read_only=True)
    developer_dev_rule_feedbacks = Development_Rule_Feedback_Serializer(many=True, read_only=True) 
    developer_dev_rules = Development_Rule_Serializer(many=True, read_only=True) 
    developer_team_memberships = Team_Member_Serializer(many=True, read_only=True)
    developer_resource_management = Resource_Manager_Serializer(many=True, read_only=True)
    developer_integration_recommended_adaptations = Recommended_Adaptations_Serializer(many=True, read_only=True)
    developer_integration_outcomes = Integration_Outcome_Serializer(many=True, read_only=True)
    allocated_integration_tools = Integration_Tool_Allocation_Serializer(many=True, read_only=True)
    developer_integration_tools = Service_Integration_Tool_Serializer(many=True, read_only=True)

    class Meta:
        model = Developer
        fields = '__all__'
 
class Feedback_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Feedback
        fields = '__all__'

class Project_Serializer(serializers.HyperlinkedModelSerializer):
    project_product_releases = Product_Release_Serializer(many=True, read_only=True)
    project_plans = Project_Plan_Serializer(many=True, read_only=True)
    project_managers = Project_Manager_Serializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

class Project_Phase_Serializer(serializers.ModelSerializer):   
    project_phase_projects = Project_Serializer(many=True, read_only=True) 
    class Meta:
        model = Project_Phase
        fields = '__all__'