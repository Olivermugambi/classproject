from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'developers', views.Developer_ViewSet)
router.register(r'sprints/(?P<id>\d+)', views.Sprint_ViewSet)
router.register(r'sprint_backlogs/(?P<id>\d+)', views.Sprint_Backlog_ViewSet)
router.register(r'sprint_backlog_allocations/(?P<id>\d+)', views.Sprint_Backlog_Allocations_ViewSet)
router.register(r'daily_srums/(?P<id>\d+)', views.Daily_Scrum_ViewSet)
router.register(r'sprint_reviews/(?P<id>\d+)', views.Sprint_Review_ViewSet)
router.register(r'sprint_retrospectives/(?P<id>\d+)', views.Sprint_Retrospective_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]