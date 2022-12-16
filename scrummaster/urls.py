from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'contact_person_status/', views.Contact_Person_Status_ViewSet)
router.register(r'contact_person/(?P<id>\d+)', views.Contact_Person_ViewSet)
router.register(r'project_phase/', views.Project_Phase_Viewset)
router.register(r'project_manager/(?P<id>\d+)', views.Project_Manager_ViewSet)
router.register(r'project/(?P<id>\d+)', views.Project_ViewSet)
router.register(r'feedback/(?P<id>\d+)', views.Feedback_ViewSet)
router.register(r'priority/', views.Priority_Viewset)
router.register(r'project_plan_status/', views.Plan_Status_Viewset)
router.register(r'project_plan/(?P<id>\d+)', views.Project_Plan_Viewset)
router.register(r'risk_status/', views.Risk_Status_Viewset)
router.register(r'project_plan_risk/(?P<id>\d+)', views.Project_Plan_Risk_Viewset)
router.register(r'development_status/', views.Development_Status_Viewset)
router.register(r'project_development/(?P<id>\d+)', views.Project_Development_Viewset)
router.register(r'team_member_role/', views.Team_Member_Role_Viewset)
router.register(r'team_member_status/', views.Team_Member_Status_Viewset)
router.register(r'development_team_status/', views.Development_Team_Status_Viewset)
router.register(r'development_team/(?P<id>\d+)', views.Development_Team_Viewset)
router.register(r'team_member/(?P<id>\d+)', views.Team_Member_Viewset)
router.register(r'development_rule/(?P<id>\d+)', views.Development_Rule_Viewset)
router.register(r'development_rule_feedback/(?P<id>\d+)', views.Development_Rule_Feedback_Viewset)
router.register(r'release_status/', views.Release_Status_Viewset)
router.register(r'product_release/(?P<id>\d+)', views.Product_Release_Viewset)
router.register(r'release_feature/(?P<id>\d+)', views.Release_Feature_Viewset)
router.register(r'release_strategy/(?P<id>\d+)', views.Release_Strategy_Viewset)
router.register(r'release_backlog/(?P<id>\d+)', views.Release_Backlog_Viewset)

urlpatterns = [
    path('', include(router.urls)),
]