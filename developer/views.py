from rest_framework import viewsets
from .serializers import *
from .models import *


class Developer_ViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all().order_by('developer_name')
    serializer_class = Developer_Serializer

class Sprint_ViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all().order_by('expected_outcome')
    serializer_class = Sprint_Serializer

#    def get_queryset(self):
#        id = self.request.GET.get('id')
#        developer, created = Developer.objects.get_or_create(id=id)
#        return Sprint_Backlog_Allocations.objects.filter(developer=developer).order_by('creation_date')

class Sprint_Backlog_ViewSet(viewsets.ModelViewSet):
    queryset = Sprint_Backlog.objects.all().order_by('creation_date')
    serializer_class = Sprint_Backlog_Serializer

class Sprint_Backlog_Allocations_ViewSet(viewsets.ModelViewSet):
    queryset = Sprint_Backlog_Allocations.objects.all().order_by('creation_date')
    serializer_class = Sprint_Backlog_Allocations_Serializer

class Daily_Scrum_ViewSet(viewsets.ModelViewSet):
    queryset = Daily_Scrum.objects.all().order_by('date')
    serializer_class = Daily_Scrum_Serializer

class Sprint_Review_ViewSet(viewsets.ModelViewSet):
    queryset = Sprint_Review.objects.all().order_by('creation_date')
    serializer_class = Sprint_Review_Serializer

class Sprint_Retrospective_ViewSet(viewsets.ModelViewSet):
    queryset = Sprint_Retrospective.objects.all().order_by('creation_date')
    serializer_class = Sprint_Retrospective_Serializer
      
class Project_ViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('project_name')
    serializer_class = Project_Serializer

class Feedback_ViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all().order_by('date_received')
    serializer_class = Feedback_Serializer

class Project_Phase_Viewset(viewsets.ModelViewSet):
    queryset = Project_Phase.objects.all().order_by('project_phase')
    serializer_class = Project_Phase_Serializer

