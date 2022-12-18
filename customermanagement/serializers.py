# The serializer class prepares the json for the responses based on the customer model
from rest_framework import serializers
from developer.serializers import *
from .models import *

# the serializers for the customer models
class Product_Requirements_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product_Requirements
        fields = '__all__'

class Customer_Product_Serializer(serializers.HyperlinkedModelSerializer):
    product_requirements = Product_Requirements_Serializer(many=True, read_only=True)
    product_feedbacks = Feedback_Serializer(many=True, read_only=True)
    product_projects = Project_Serializer(many=True, read_only=True)

    class Meta:
        model = Customer_Product
        fields = '__all__'

class Customer_Message_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Customer_Message
        fields = '__all__'

class Contact_Person_Status_Serializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Contact_Person_Status
        fields = '__all__'

class Contact_Person_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact_Person
        fields = '__all__'

class Customer_Profile_Serializer(serializers.HyperlinkedModelSerializer):
    customer_products = Customer_Product_Serializer(many=True, read_only=True)
    customer_messages = Customer_Message_Serializer(many=True, read_only=True)
    customer_contact_persons = Contact_Person_Serializer(many=True, read_only=True) 

    class Meta:
        model = Customer_Profile
        fields = '__all__'

class User_Serializer(serializers.ModelSerializer):  
    message_recipient =  Customer_Message_Serializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'