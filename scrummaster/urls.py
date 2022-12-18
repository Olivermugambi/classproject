from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'project_manager', views.Project_Manager_ViewSet)
router.register(r'priority', views.Priority_Viewset)
router.register(r'project_plan_status', views.Plan_Status_Viewset)
router.register(r'project_plan', views.Project_Plan_Viewset)
router.register(r'risk_status', views.Risk_Status_Viewset)
router.register(r'project_plan_risk', views.Project_Plan_Risk_Viewset)
router.register(r'development_status', views.Development_Status_Viewset)
router.register(r'project_development', views.Project_Development_Viewset)
router.register(r'team_member_role', views.Team_Member_Role_Viewset)
router.register(r'team_member_status', views.Team_Member_Status_Viewset)
router.register(r'development_team_status', views.Development_Team_Status_Viewset)
router.register(r'development_team', views.Development_Team_Viewset)
router.register(r'team_member', views.Team_Member_Viewset)
router.register(r'development_rule', views.Development_Rule_Viewset)
router.register(r'development_rule_feedback', views.Development_Rule_Feedback_Viewset)
router.register(r'release_status', views.Release_Status_Viewset)
router.register(r'product_release', views.Product_Release_Viewset)
router.register(r'release_feature', views.Release_Feature_Viewset)
router.register(r'release_strategy', views.Release_Strategy_Viewset)
router.register(r'release_backlog', views.Release_Backlog_Viewset)

urlpatterns = [
    path('', include(router.urls)),
]