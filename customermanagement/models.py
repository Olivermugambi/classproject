from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Customer_Type(models.Model):
    customer_type = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created', default=datetime.now())

class Customer_Status(models.Model):
    customer_status = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created', default=datetime.now())

class Customer_Profile(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)
    customer_telephone = models.CharField(max_length=200)
    customer_type = models.ForeignKey(Customer_Type, on_delete=models.CASCADE, null=True)
    customer_status = models.ForeignKey(Customer_Status, on_delete=models.CASCADE, null=True)
    customer_address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    registration_number = models.CharField(max_length=200, null=True)
    postal_code = models.CharField(max_length=200, null=True)
    created_on= models.DateTimeField('date created', default=datetime.now())

class Message_Type(models.Model):
    message_type = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created', default=datetime.now())

class Message_Status(models.Model):
    message_status = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created', default=datetime.now())

class Customer_Message(models.Model):
    customer = models.ForeignKey(Customer_Profile, on_delete=models.CASCADE, null=True)
    message_subject = models.CharField(max_length=200)
    message_body = models.CharField(max_length=200)
    recepient = models.ForeignKey(User, on_delete=models.CASCADE)
    message_status = models.ForeignKey(Message_Status, on_delete=models.CASCADE, null=True)
    date_sent = models.DateTimeField('date sent', default=datetime.now())
    date_received = models.DateTimeField('date received', null=True)

class Product_Type(models.Model):
    product_type = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created', default=datetime.now())


class Customer_Product(models.Model):
    customer = models.ForeignKey(Customer_Profile, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=200)
    product_type = models.ForeignKey(Product_Type, on_delete=models.CASCADE, null=True)
    product_description = models.TextField(null=True)
    created_on= models.DateTimeField('date created', default=datetime.now())

class Product_Requirements(models.Model):
    product = models.ForeignKey(Customer_Product, on_delete=models.CASCADE, null=True)
    requirement_description = models.TextField()
    recommended_test = models.TextField(null=True)
    created_on= models.DateTimeField('date created', default=datetime.now())



