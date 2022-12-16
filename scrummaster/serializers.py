# The serializer class prepares the json for the responses based on the scrum model
from rest_framework import serializers

from .models import *

# the serializers for the scrummaster and project manager models
class Customer_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Customer_Profile
        fields = ('customer_name',)

class Developer_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Developer
        fields = ('developer_name',)

class Contact_Person_Status_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Contact_Person_Status
        fields = ('status',)

class Contact_Person_Serializer(serializers.HyperlinkedModelSerializer):
    customer = Customer_Serializer()
    status = Contact_Person_Status_Serializer()

    class Meta:
        model = Contact_Person
        fields = ('name', 'email', 'telephone', 'address', 'status', 'customer', 
        'registration_date')

    def create(self, validated_data):
        customer, created = Customer_Profile.objects.get_or_create(customer_name=validated_data.pop('customer'))
        status, created = Contact_Person_Status.objects.get_or_create(status=validated_data.pop('status'))
        instance = Contact_Person.objects.create(**validated_data, customer=customer, status=status)
        return instance

class Project_Phase_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Project_Phase
        fields = ('project_phase',)

class Customer_Product_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Customer_Product
        fields = ('product_name',)

class Project_Serializer(serializers.HyperlinkedModelSerializer):
    product = Customer_Product_Serializer()
    project_phase = Project_Phase_Serializer()

    class Meta:
        model = Project
        fields = ('product', 'project_name', 'start_date', 'deadline', 'project_phase')

    def create(self, validated_data):
        product, created = Customer_Product.objects.get_or_create(product_name=validated_data.pop('product'))
        project_phase, created = Project_Phase.objects.get_or_create(project_phase=validated_data.pop('project_phase'))
        instance = Project.objects.create(**validated_data, product=product, project_phase=project_phase)
        return instance
        

class Feedback_Serializer(serializers.HyperlinkedModelSerializer):
    product = Customer_Product_Serializer()
    
    class Meta:
        model = Feedback
        fields = ('product', 'subject', 'feedback', 'comments', 'date_received')

    def create(self, validated_data):
        product, created = Customer_Product.objects.get_or_create(product_name=validated_data.pop('product'))
        instance = Feedback.objects.create(**validated_data, product=product)
        return instance

class Priority_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Priority
        fields = ('priority',)

class Plan_Status_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Plan_Status
        fields = ('status',)

class Project_Name_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Project
        fields = ('project_name',)

class Project_Manager_Form_Serializer(serializers.ModelSerializer):  
    project_manager = Developer_Serializer()
    project = Project_Name_Serializer()

    class Meta:
        model = Project_Manager
        fields = ('project_manager','project')

    def create(self, validated_data):
        project_manager, created = Developer.objects.get_or_create(developer_name=validated_data.pop('project_manager'))
        project, created = Project.objects.get_or_create(project_name=validated_data.pop('project'))
        instance = Feedback.objects.create(**validated_data, project_manager=project_manager,
            project=project)
        return instance

class Project_Manager_Serializer(serializers.ModelSerializer):  
    project_manager = Developer_Serializer()

    class Meta:
        model = Project_Manager
        fields = ('project_manager',)

class Project_Plan_Serializer(serializers.HyperlinkedModelSerializer):
    project = Project_Name_Serializer()
    plan_priority = Priority_Serializer()
    plan_manager = Project_Manager_Serializer()
    plan_status = Plan_Status_Serializer()
    
    class Meta:
        model = Project_Plan
        fields = ('project', 'plan', 'deliverable', 'deadline', 'plan_priority', 'plan_manager', 'creation_date', 'plan_status')

    def create(self, validated_data):
        project, created = Project.objects.get_or_create(project_name=validated_data.pop('project'))
        plan_priority, created = Priority.objects.get_or_create(priority=validated_data.pop('plan_priority'))
        plan_manager, created = Project_Manager.objects.get_or_create(project_manager=validated_data.pop('project_manager'))
        plan_status, created = Plan_Status.objects.get_or_create(status=validated_data.pop('plan_status'))
        instance = Project_Plan.objects.create(**validated_data, project=project, plan_priority=plan_priority, 
            plan_manager=plan_manager, plan_status=plan_status)
        return instance

class Risk_Status_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Risk_Status
        fields = ('status',)

class Project_Plan_Field_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Project_Plan
        fields = ('plan',)

class Project_Plan_Risk_Serializer(serializers.HyperlinkedModelSerializer):
    project_plan = Project_Plan_Field_Serializer()
    risk_manager = Project_Manager_Serializer()
    risk_status = Risk_Status_Serializer()
    
    class Meta:
        model = Project_Plan_Risk
        fields = ('project_plan', 'risk', 'risk_priority', 'risk_manager', 'creation_date', 'risk_status')

    def create(self, validated_data):
        project_plan, created = Project_Plan.objects.get_or_create(plan=validated_data.pop('project_plan'))
        risk_manager, created = Project_Manager.objects.get_or_create(project_manager=validated_data.pop('risk_manager'))
        risk_status, created = Risk_Status.objects.get_or_create(status=validated_data.pop('risk_status'))
        instance = Project_Plan_Risk.objects.create(**validated_data, project_plan=project_plan, 
            risk_manager=risk_manager, risk_status=risk_status)
        return instance

class Development_Status_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Development_Status
        fields = ('status',)

class Project_Development_Serializer(serializers.HyperlinkedModelSerializer):
    development_plan = Project_Plan_Field_Serializer()
    scrum_master = Project_Manager_Serializer()
    development_status = Development_Status_Serializer()
    
    class Meta:
        model = Project_Development
        fields = ('development_plan', 'required_skills', 'deadline', 'scrum_master', 'creation_date', 'development_status')

    def create(self, validated_data):
        development_plan, created = Project_Plan.objects.get_or_create(plan=validated_data.pop('development_plan'))
        scrum_master, created = Project_Manager.objects.get_or_create(project_manager=validated_data.pop('scrum_master'))
        development_status, created = Development_Status.objects.get_or_create(status=validated_data.pop('development_status'))
        instance = Project_Development.objects.create(**validated_data, development_plan=development_plan, 
            scrum_master=scrum_master, development_status=development_status)
        return instance

class Team_Member_Role_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Team_Member_Role
        fields = ('role',)

class Team_Member_Status_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Team_Member_Status
        fields = ('status',)

class Development_Team_Status_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Development_Team_Status
        fields = ('status',)

class Project_Development_Field_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Project_Development
        fields = ('development_plan',)

class Development_Team_Serializer(serializers.HyperlinkedModelSerializer):
    project_development = Project_Development_Field_Serializer()
    team_status = Development_Team_Status_Serializer()
    
    class Meta:
        model = Development_Team
        fields = ('project_development', 'team_name', 'creation_date', 'team_status')

    def create(self, validated_data):
        dev_plan, created = Project_Plan.objects.get_or_create(plan=validated_data.pop('project_development'))
        project_development, created = Project_Development.objects.get_or_create(development_plan=dev_plan)
        team_status, created = Development_Team_Status.objects.get_or_create(status=validated_data.pop('team_status'))
        instance = Development_Team.objects.create(**validated_data, project_development=project_development, 
            team_status=team_status)
        return instance

class Development_Team_Field_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Development_Team
        fields = ('team_name',)

class Team_Member_Serializer(serializers.HyperlinkedModelSerializer):
    team = Development_Team_Field_Serializer()
    developer = Developer_Serializer()
    member_role = Team_Member_Role_Serializer()
    member_status = Team_Member_Status_Serializer()
    
    class Meta:
        model = Team_Member
        fields = ('team', 'developer', 'member_role', 'creation_date', 'member_status', 'start_date', 'end_date')

    def create(self, validated_data):
        team, created = Development_Team.objects.get_or_create(team_name=validated_data.pop('team'))
        developer, created = Developer.objects.get_or_create(developer_name=validated_data.pop('developer'))
        member_role, created = Team_Member_Role.objects.get_or_create(role=validated_data.pop('member_role'))
        member_status, created = Team_Member_Status.objects.get_or_create(status=validated_data.pop('member_status'))
        instance = Team_Member.objects.create(**validated_data, team=team, developer=developer,
            member_role=member_role, member_status=member_status)
        return instance

class Development_Rule_Serializer(serializers.HyperlinkedModelSerializer):
    project_development = Project_Development_Field_Serializer()
    made_by = Project_Manager_Serializer()
    
    class Meta:
        model = Development_Rule
        fields = ('project_development', 'rule', 'justification', 'creation_date', 'made_by')

    def create(self, validated_data):
        project_development, created = Project_Development.objects.get_or_create(development_plan=validated_data.pop('project_development'))
        made_by, created = Project_Manager.objects.get_or_create(project_manager=validated_data.pop('made_by'))
        instance = Development_Rule.objects.create(**validated_data, project_development=project_development, 
            made_by=made_by)
        return instance

class Development_Rule_Field_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Development_Rule
        fields = ('rule',)

class Development_Rule_Feedback_Serializer(serializers.HyperlinkedModelSerializer):
    rule = Development_Rule_Field_Serializer()
    developer = Developer_Serializer()
    
    class Meta:
        model = Development_Rule_Feedback
        fields = ('rule', 'developer', 'feedback', 'creation_date')

    def create(self, validated_data):
        rule, created = Development_Rule.objects.get_or_create(rule=validated_data.pop('rule'))
        developer, created = Developer.objects.get_or_create(developer_name=validated_data.pop('developer'))
        instance = Development_Rule_Feedback.objects.create(**validated_data, rule=rule, 
            developer=developer)
        return instance

class Release_Status_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Release_Status
        fields = ('status',)

class Product_Release_Serializer(serializers.HyperlinkedModelSerializer):
    project = Project_Name_Serializer()
    release_status = Release_Status_Serializer()
    
    class Meta:
        model = Product_Release
        fields = ('project', 'release_definition', 'release_date', 'release_status')

    def create(self, validated_data):
        project, created = Project.objects.get_or_create(project_name=validated_data.pop('project'))
        release_status, created = Release_Status.objects.get_or_create(status=validated_data.pop('release_status'))
        instance = Product_Release.objects.create(**validated_data, project=project, release_status=release_status)
        return instance

class Product_Release_Field_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Product_Release
        fields = ('release_definition',)
        
class Release_Feature_Serializer(serializers.HyperlinkedModelSerializer):
    release = Product_Release_Field_Serializer()
    priority = Priority_Serializer()
    
    class Meta:
        model = Release_Feature
        fields = ('feature', 'priority', 'release_date', 'release')

    def create(self, validated_data):
        release, created = Product_Release.objects.get_or_create(release_definition=validated_data.pop('release'))
        priority, created = Priority.objects.get_or_create(priority=validated_data.pop('priority'))
        instance = Release_Feature.objects.create(**validated_data, release=release, priority=priority)
        return instance

class Release_Feature_Field_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Release_Feature
        fields = ('feature',)

class Release_Strategy_Serializer(serializers.HyperlinkedModelSerializer):
    manager = Project_Manager_Serializer()
    release = Product_Release_Field_Serializer()
    feature = Release_Feature_Field_Serializer()

    class Meta:
        model = Release_Strategy
        fields = ('strategy', 'manager', 'creation_date', 'release', 'feature')

    def create(self, validated_data):
        manager, created = Project_Manager.objects.get_or_create(project_manager=validated_data.pop('manager'))
        release, created = Product_Release.objects.get_or_create(release_definition=validated_data.pop('release'))
        feature, created = Release_Feature.objects.get_or_create(feature=validated_data.pop('feature'))
        instance = Release_Strategy.objects.create(**validated_data, manager=manager,
            release=release, feature=feature)
        return instance

class Release_Strategy_Field_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Release_Strategy
        fields = ('strategy',)

class Release_Backlog_Serializer(serializers.HyperlinkedModelSerializer):
    manager = Project_Manager_Serializer()
    strategy = Release_Strategy_Serializer()

    class Meta:
        model = Release_Backlog
        fields = ('backlog', 'manager', 'creation_date', 'strategy')

    def create(self, validated_data):
        manager, created = Project_Manager.objects.get_or_create(project_manager=validated_data.pop('manager'))
        strategy, created = Release_Strategy.objects.get_or_create(strategy=validated_data.pop('strategy'))
        instance = Release_Backlog.objects.create(**validated_data, manager=manager,
            strategy=strategy)
        return instance