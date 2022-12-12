from rest_framework import viewsets
from .serializers import *


class Customer_Profile_ViewSet(viewsets.ModelViewSet):
    queryset = Customer_Profile.objects.all().order_by('customer_name')
    serializer_class = Customer_Profile_Serializer

class Customer_Message_ViewSet(viewsets.ModelViewSet):
    queryset = Customer_Message.objects.all().order_by('date_sent')
    serializer_class = Customer_Message_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        customer, created = Customer_Profile.objects.get_or_create(id=id)
        return Customer_Message.objects.filter(customer=customer).order_by('date_sent')

class Customer_Product_ViewSet(viewsets.ModelViewSet):
    queryset = Customer_Product.objects.all().order_by('product_name')
    serializer_class = Customer_Product_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        customer, created = Customer_Profile.objects.get_or_create(id=id)
        return Customer_Product.objects.filter(customer=customer).order_by('product_name')

class Product_Requirements_ViewSet(viewsets.ModelViewSet):
    queryset = Product_Requirements.objects.all().order_by('created_on')
    serializer_class = Product_Requirements_Serializer

    def get_queryset(self):
        id = self.request.GET.get('id')
        product, created = Customer_Product.objects.get_or_create(id=id)
        return Product_Requirements.objects.filter(product=product).order_by('created_on')


