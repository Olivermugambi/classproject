from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'customers', views.Customer_Profile_ViewSet)
router.register(r'customer_messages', views.Customer_Message_ViewSet)
router.register(r'customer_products', views.Customer_Product_ViewSet)
router.register(r'product_requirements', views.Product_Requirements_ViewSet)
router.register(r'contact_person_status', views.Contact_Person_Status_ViewSet)
router.register(r'contact_person', views.Contact_Person_ViewSet)


urlpatterns = [
    path('', include(router.urls)),
]