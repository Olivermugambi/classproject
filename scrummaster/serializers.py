# The serializer class prepares the json for the responses based on the scrum model
from rest_framework import serializers
from .models import *

# the serializers for the scrummaster and project manager models
class Release_Backlog_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Release_Backlog
        fields = '__all__'

class Release_Strategy_Serializer(serializers.HyperlinkedModelSerializer):
    strategy_release_backlogs = Release_Backlog_Serializer(many=True, read_only=True)

    class Meta:
        model = Release_Strategy
        fields = '__all__'

class Release_Feature_Serializer(serializers.HyperlinkedModelSerializer):
    feature_release_strategies = Release_Strategy_Serializer(many=True, read_only=True)

    class Meta:
        model = Release_Feature
        fields = '__all__'

class Product_Release_Serializer(serializers.HyperlinkedModelSerializer):
    release_strategies = Release_Strategy_Serializer(many=True, read_only=True)
    release_features = Release_Feature_Serializer(many=True, read_only=True)

    class Meta:
        model = Product_Release
        fields = '__all__'

class Release_Status_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Release_Status
        fields = '__all__'

class Development_Rule_Feedback_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Development_Rule_Feedback
        fields = '__all__'

class Development_Rule_Serializer(serializers.HyperlinkedModelSerializer):
    dev_rule_feedbacks = Development_Rule_Feedback_Serializer(many=True, read_only=True)

    class Meta:
        model = Development_Rule
        fields = '__all__'

class Team_Member_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Team_Member
        fields = '__all__'

class Development_Team_Serializer(serializers.HyperlinkedModelSerializer):
    team_members = Team_Member_Serializer(many=True, read_only=True)

    class Meta:
        model = Development_Team
        fields = '__all__'

class Team_Member_Status_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Team_Member_Status
        fields = '__all__'

class Development_Team_Status_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Development_Team_Status
        fields = '__all__'

class Team_Member_Role_Serializer(serializers.ModelSerializer): 
    role_team_members = Team_Member_Serializer(many=True, read_only=True)

    class Meta:
        model = Team_Member_Role
        fields = '__all__'

class Project_Development_Serializer(serializers.HyperlinkedModelSerializer):
    project_dev_rules = Development_Rule_Serializer(many=True, read_only=True)
    dev_teams= Development_Team_Serializer(many=True, read_only=True)

    class Meta:
        model = Project_Development
        fields = '__all__'

class Development_Status_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Development_Status
        fields = '__all__'

class Project_Plan_Risk_Serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Project_Plan_Risk
        fields = '__all__'

class Risk_Status_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Risk_Status
        fields = '__all__'

class Project_Plan_Serializer(serializers.HyperlinkedModelSerializer):
    dev_plan_implementations = Project_Development_Serializer(many=True, read_only=True)
    project_plan_risks = Project_Plan_Risk_Serializer(many=True, read_only=True)

    class Meta:
        model = Project_Plan
        fields = '__all__'

class Project_Manager_Serializer(serializers.ModelSerializer):  
    manager_release_backlogs = Release_Backlog_Serializer(many=True, read_only=True)
    manager_release_strategies = Release_Strategy_Serializer(many=True, read_only=True)
    scrummaster_project_developments = Project_Development_Serializer(many=True, read_only=True)
    manager_project_plan_risks = Project_Plan_Risk_Serializer(many=True, read_only=True)
    manager_project_plans = Project_Plan_Serializer(many=True, read_only=True)

    class Meta:
        model = Project_Manager
        fields = '__all__'

class Plan_Status_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Plan_Status
        fields = '__all__'

class Priority_Serializer(serializers.ModelSerializer):    
    priority_release_features = Release_Feature_Serializer(many=True, read_only=True)
    priority_project_plan_risks = Project_Plan_Risk_Serializer(many=True, read_only=True)
    priority_project_plans = Project_Plan_Serializer(many=True, read_only=True)

    class Meta:
        model = Priority
        fields = '__all__'



