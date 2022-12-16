from rest_framework import viewsets
from .serializers import *


class Contact_Person_Status_ViewSet(viewsets.ModelViewSet):
    queryset = Contact_Person_Status.objects.all().order_by('status')
    serializer_class = Contact_Person_Status_Serializer

class Contact_Person_ViewSet(viewsets.ModelViewSet):
    queryset = Contact_Person.objects.all().order_by('name')
    serializer_class = Contact_Person_Serializer

class Project_Phase_Viewset(viewsets.ModelViewSet):
    queryset = Project_Phase.objects.all().order_by('project_phase')
    serializer_class = Project_Phase_Serializer

class Project_Manager_ViewSet(viewsets.ModelViewSet):
    queryset = Project_Manager.objects.all().order_by('project_manager')
    serializer_class = Project_Manager_Form_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        project_manager, created = Developer.objects.get_or_create(id=id)
        return Project_Manager.objects.filter(project_manager=project_manager).order_by('project_manager')
        
class Project_ViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('project_name')
    serializer_class = Project_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        product, created = Customer_Product.objects.get_or_create(id=id)
        return Project.objects.filter(product=product).order_by('project_name')

class Feedback_ViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all().order_by('date_received')
    serializer_class = Feedback_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        product, created = Customer_Product.objects.get_or_create(id=id)
        return Feedback.objects.filter(product=product).order_by('date_received')

class Priority_Viewset(viewsets.ModelViewSet):
    queryset = Priority.objects.all().order_by('priority')
    serializer_class = Priority_Serializer

class Plan_Status_Viewset(viewsets.ModelViewSet):
    queryset = Plan_Status.objects.all().order_by('status')
    serializer_class = Plan_Status_Serializer

class Project_Plan_Viewset(viewsets.ModelViewSet):
    queryset = Project_Plan.objects.all().order_by('deadline')
    serializer_class = Project_Plan_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        project, created = Project.objects.get_or_create(id=id)
        return Project_Plan.objects.filter(project=project).order_by('deadline')

class Risk_Status_Viewset(viewsets.ModelViewSet):
    queryset = Risk_Status.objects.all().order_by('status')
    serializer_class = Risk_Status_Serializer

class Project_Plan_Risk_Viewset(viewsets.ModelViewSet):
    queryset = Project_Plan_Risk.objects.all().order_by('risk_priority')
    serializer_class = Project_Plan_Risk_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        project_plan, created = Project_Plan.objects.get_or_create(id=id)
        return Project_Plan_Risk.objects.filter(project_plan=project_plan).order_by('risk_priority')


class Development_Status_Viewset(viewsets.ModelViewSet):
    queryset = Development_Status.objects.all().order_by('status')
    serializer_class = Development_Status_Serializer

class Project_Development_Viewset(viewsets.ModelViewSet):
    queryset = Project_Development.objects.all().order_by('deadline')
    serializer_class = Project_Development_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        project_plan, created = Project_Plan.objects.get_or_create(id=id)
        return Project_Development.objects.filter(development_plan=project_plan).order_by('deadline')

class Team_Member_Role_Viewset(viewsets.ModelViewSet):
    queryset = Team_Member_Role.objects.all().order_by('role')
    serializer_class = Team_Member_Role_Serializer

class Team_Member_Status_Viewset(viewsets.ModelViewSet):
    queryset = Team_Member_Status.objects.all().order_by('status')
    serializer_class = Team_Member_Status_Serializer


class Development_Team_Status_Viewset(viewsets.ModelViewSet):
    queryset = Development_Team_Status.objects.all().order_by('status')
    serializer_class = Development_Team_Status_Serializer

class Development_Team_Viewset(viewsets.ModelViewSet):
    queryset = Development_Team.objects.all().order_by('team_name')
    serializer_class = Development_Team_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        project_development, created = Project_Development.objects.get_or_create(id=id)
        return Development_Team.objects.filter(project_development=project_development).order_by('team_name')

class Team_Member_Viewset(viewsets.ModelViewSet):
    queryset = Team_Member.objects.all().order_by('developer')
    serializer_class = Team_Member_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        team, created = Development_Team.objects.get_or_create(id=id)
        return Team_Member.objects.filter(team=team).order_by('developer')

class Development_Rule_Viewset(viewsets.ModelViewSet):
    queryset = Development_Rule.objects.all().order_by('creation_date')
    serializer_class = Development_Rule_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        project_development, created = Project_Development.objects.get_or_create(id=id)
        return Development_Rule.objects.filter(project_development=project_development).order_by('creation_date')

class Development_Rule_Feedback_Viewset(viewsets.ModelViewSet):
    queryset = Development_Rule_Feedback.objects.all().order_by('creation_date')
    serializer_class = Development_Rule_Feedback_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        rule, created = Development_Rule.objects.get_or_create(id=id)
        return Development_Rule_Feedback.objects.filter(rule=rule).order_by('creation_date')

class Release_Status_Viewset(viewsets.ModelViewSet):
    queryset = Release_Status.objects.all().order_by('status')
    serializer_class = Release_Status_Serializer

class Product_Release_Viewset(viewsets.ModelViewSet):
    queryset = Product_Release.objects.all().order_by('release_date')
    serializer_class = Product_Release_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        project, created = Project.objects.get_or_create(id=id)
        return Product_Release.objects.filter(project=project).order_by('release_date')

class Release_Feature_Viewset(viewsets.ModelViewSet):
    queryset = Release_Feature.objects.all().order_by('release_date')
    serializer_class = Release_Feature_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        release, created = Product_Release.objects.get_or_create(id=id)
        return Release_Feature.objects.filter(release=release).order_by('release_date')

class Release_Strategy_Viewset(viewsets.ModelViewSet):
    queryset = Release_Strategy.objects.all().order_by('feature')
    serializer_class = Release_Strategy_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        manager, created = Project_Manager.objects.get_or_create(id=id)
        return Release_Strategy.objects.filter(manager=manager).order_by('feature')

class Release_Backlog_Viewset(viewsets.ModelViewSet):
    queryset = Release_Backlog.objects.all().order_by('strategy')
    serializer_class = Release_Backlog_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        manager, created = Project_Manager.objects.get_or_create(id=id)
        return Release_Backlog.objects.filter(manager=manager).order_by('strategy')