from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'resources', views.Resource_ViewSet)
router.register(r'resource_statuses', views.Resource_Status_ViewSet)
router.register(r'resource_types', views.Resource_Type_ViewSet)
router.register(r'resource_managers', views.Resource_Manager_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]