from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'customers', views.Customer_Profile_ViewSet)
router.register(r'customer_messages/(?P<id>\d+)', views.Customer_Message_ViewSet)
router.register(r'customer_products/(?P<id>\d+)', views.Customer_Product_ViewSet)
router.register(r'product_requirements/(?P<id>\d+)', views.Product_Requirements_ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]