from rest_framework import viewsets
from .serializers import *

class Project_Manager_ViewSet(viewsets.ModelViewSet):
    queryset = Project_Manager.objects.all().order_by('project_manager')
    serializer_class = Project_Manager_Serializer

class Priority_Viewset(viewsets.ModelViewSet):
    queryset = Priority.objects.all().order_by('priority')
    serializer_class = Priority_Serializer

class Plan_Status_Viewset(viewsets.ModelViewSet):
    queryset = Plan_Status.objects.all().order_by('status')
    serializer_class = Plan_Status_Serializer

class Project_Plan_Viewset(viewsets.ModelViewSet):
    queryset = Project_Plan.objects.all().order_by('deadline')
    serializer_class = Project_Plan_Serializer

class Risk_Status_Viewset(viewsets.ModelViewSet):
    queryset = Risk_Status.objects.all().order_by('status')
    serializer_class = Risk_Status_Serializer

class Project_Plan_Risk_Viewset(viewsets.ModelViewSet):
    queryset = Project_Plan_Risk.objects.all().order_by('risk_priority')
    serializer_class = Project_Plan_Risk_Serializer

class Development_Status_Viewset(viewsets.ModelViewSet):
    queryset = Development_Status.objects.all().order_by('status')
    serializer_class = Development_Status_Serializer

class Project_Development_Viewset(viewsets.ModelViewSet):
    queryset = Project_Development.objects.all().order_by('deadline')
    serializer_class = Project_Development_Serializer

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

class Team_Member_Viewset(viewsets.ModelViewSet):
    queryset = Team_Member.objects.all().order_by('developer')
    serializer_class = Team_Member_Serializer

class Development_Rule_Viewset(viewsets.ModelViewSet):
    queryset = Development_Rule.objects.all().order_by('creation_date')
    serializer_class = Development_Rule_Serializer

class Development_Rule_Feedback_Viewset(viewsets.ModelViewSet):
    queryset = Development_Rule_Feedback.objects.all().order_by('creation_date')
    serializer_class = Development_Rule_Feedback_Serializer

class Release_Status_Viewset(viewsets.ModelViewSet):
    queryset = Release_Status.objects.all().order_by('status')
    serializer_class = Release_Status_Serializer

class Product_Release_Viewset(viewsets.ModelViewSet):
    queryset = Product_Release.objects.all().order_by('release_date')
    serializer_class = Product_Release_Serializer

class Release_Feature_Viewset(viewsets.ModelViewSet):
    queryset = Release_Feature.objects.all().order_by('release_date')
    serializer_class = Release_Feature_Serializer

class Release_Strategy_Viewset(viewsets.ModelViewSet):
    queryset = Release_Strategy.objects.all().order_by('feature')
    serializer_class = Release_Strategy_Serializer

class Release_Backlog_Viewset(viewsets.ModelViewSet):
    queryset = Release_Backlog.objects.all().order_by('strategy')
    serializer_class = Release_Backlog_Serializer
