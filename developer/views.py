from rest_framework import viewsets
from .serializers import *


class Developer_ViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all().order_by('developer_name')
    serializer_class = Developer_Serializer

class Sprint_ViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all().order_by('start_date')
    serializer_class = Sprint_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        developer, created = Developer.objects.get_or_create(id=id)
        return Sprint.objects.filter(added_by=developer).order_by('start_date')

class Sprint_Backlog_ViewSet(viewsets.ModelViewSet):
    queryset = Sprint_Backlog.objects.all().order_by('creation_date')
    serializer_class = Sprint_Backlog_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        developer, created = Developer.objects.get_or_create(id=id)
        return Sprint_Backlog.objects.filter(added_by=developer).order_by('creation_date')

class Sprint_Backlog_Allocations_ViewSet(viewsets.ModelViewSet):
    queryset = Sprint_Backlog_Allocations.objects.all().order_by('creation_date')
    serializer_class = Sprint_Backlog_Allocations_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        developer, created = Developer.objects.get_or_create(id=id)
        return Sprint_Backlog_Allocations.objects.filter(developer=developer).order_by('creation_date')

class Daily_Scrum_ViewSet(viewsets.ModelViewSet):
    queryset = Daily_Scrum.objects.all().order_by('date')
    serializer_class = Daily_Scrum_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        sprint_backlog, created = Sprint_Backlog.objects.get_or_create(id=id)
        return Daily_Scrum.objects.filter(sprint_backlog=sprint_backlog).order_by('date')

class Sprint_Review_ViewSet(viewsets.ModelViewSet):
    queryset = Sprint_Review.objects.all().order_by('creation_date')
    serializer_class = Sprint_Review_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        sprint, created = Sprint.objects.get_or_create(id=id)
        return Sprint_Review.objects.filter(sprint=sprint).order_by('creation_date')

class Sprint_Retrospective_ViewSet(viewsets.ModelViewSet):
    queryset = Sprint_Retrospective.objects.all().order_by('creation_date')
    serializer_class = Sprint_Retrospective_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        sprint, created = Sprint.objects.get_or_create(id=id)
        return Sprint_Retrospective.objects.filter(sprint=sprint).order_by('creation_date')