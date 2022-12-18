from rest_framework import viewsets
from .serializers import *


class Customer_Profile_ViewSet(viewsets.ModelViewSet):
    queryset = Customer_Profile.objects.all().order_by('customer_name')
    serializer_class = Customer_Profile_Serializer

class Customer_Message_ViewSet(viewsets.ModelViewSet):
    queryset = Customer_Message.objects.all().order_by('date_sent')
    serializer_class = Customer_Message_Serializer

class Contact_Person_Status_ViewSet(viewsets.ModelViewSet):
    queryset = Contact_Person_Status.objects.all().order_by('status')
    serializer_class = Contact_Person_Status_Serializer

class Contact_Person_ViewSet(viewsets.ModelViewSet):
    queryset = Contact_Person.objects.all().order_by('name')
    serializer_class = Contact_Person_Serializer
    
class Customer_Product_ViewSet(viewsets.ModelViewSet):
    queryset = Customer_Product.objects.all().order_by('product_name')
    serializer_class = Customer_Product_Serializer

class Product_Requirements_ViewSet(viewsets.ModelViewSet):
    queryset = Product_Requirements.objects.all().order_by('created_on')
    serializer_class = Product_Requirements_Serializer


