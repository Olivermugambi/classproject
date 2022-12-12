# The serializer class prepares the json for the responses based on the customer model
from rest_framework import serializers

from .models import *

# the serializers for the customer models
class Customer_Profile_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer_Profile
        fields = ('customer_name', 'customer_email', 'customer_telephone', 'customer_type', 'customer_status', 
        'customer_address', 'city', 'url', 'registration_number', 'postal_code', 'created_on')

class User_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ('email',)

class Customer_Serializer(serializers.ModelSerializer):    
    class Meta:
        model = Customer_Profile
        fields = ('customer_email',)

class Customer_Message_Serializer(serializers.HyperlinkedModelSerializer):
    recepient = User_Serializer()
    customer = Customer_Serializer()

    class Meta:
        model = Customer_Message
        fields = ('message_subject', 'message_body', 'recepient', 'message_status', 
        'date_sent', 'date_received', 'customer')

class Customer_Product_Serializer(serializers.HyperlinkedModelSerializer):
    customer = Customer_Serializer() 

    class Meta:
        model = Customer_Product
        fields = ('product_name', 'product_type', 'product_description', 'created_on', 'customer')

class Product_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer_Product
        fields = ('product_name',)

class Product_Requirements_Serializer(serializers.HyperlinkedModelSerializer):
    product = Product_Serializer()

    class Meta:
        model = Product_Requirements
        fields = ('product', 'requirement_description', 'recommended_test', 'created_on')