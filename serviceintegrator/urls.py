from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'service_pipelines', views.Service_Pipeline_ViewSet)
router.register(r'pipeline_item_statuses', views.Service_Pipeline_Item_Status_ViewSet)
router.register(r'service_types', views.Service_Type_ViewSet)
router.register(r'pipeline_items', views.Service_Pipeline_Item_ViewSet)
router.register(r'integration_statuses', views.Service_Integration_Status_ViewSet)
router.register(r'service_integrations', views.Service_Integration_ViewSet)
router.register(r'service_integrators', views.Service_Integrator_ViewSet)
router.register(r'integration_items', views.Service_Integration_Item_ViewSet)
router.register(r'integration_tool_statuses', views.Integration_Tool_Status_ViewSet)
router.register(r'integration_tool_types', views.Integration_Tool_Type_ViewSet)
router.register(r'service_integration_tools', views.Service_Integration_Tool_ViewSet)
router.register(r'tool_allocation_statuses', views.Tool_Allocation_Status_ViewSet)
router.register(r'tool_allocations', views.Integration_Tool_Allocation_ViewSet)
router.register(r'progress', views.Progress_ViewSet)
router.register(r'integration_progress', views.Integration_Progress_ViewSet)
router.register(r'integration_outcomes', views.Integration_Outcome_ViewSet)
router.register(r'recommended_adaptations', views.Recommended_Adaptations_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]