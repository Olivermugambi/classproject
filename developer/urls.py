from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'developers', views.Developer_ViewSet)
router.register(r'sprints', views.Sprint_ViewSet)
router.register(r'sprint_backlogs', views.Sprint_Backlog_ViewSet)
router.register(r'sprint_backlog_allocations', views.Sprint_Backlog_Allocations_ViewSet)
router.register(r'daily_srums', views.Daily_Scrum_ViewSet)
router.register(r'sprint_reviews', views.Sprint_Review_ViewSet)
router.register(r'sprint_retrospectives', views.Sprint_Retrospective_ViewSet)
router.register(r'project_phase', views.Project_Phase_Viewset)
router.register(r'project', views.Project_ViewSet)
router.register(r'feedback', views.Feedback_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]