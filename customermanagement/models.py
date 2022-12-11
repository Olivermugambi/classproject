from django.db import models
from django.contrib.auth.models import User

class Customer_Type(models.Model):
    customer_type = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created')

class Customer_Status(models.Model):
    customer_status = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created')

class Customer_Profile(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)
    customer_telephone = models.CharField(max_length=200)
    customer_type = models.ForeignKey(Customer_Type, on_delete=models.CASCADE)
    customer_status = models.ForeignKey(Customer_Status, on_delete=models.CASCADE)
    customer_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    registration_number = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)

class Message_Type(models.Model):
    message_type = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created')

class Message_Status(models.Model):
    message_status = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created')

class Customer_Message(models.Model):
    message_token = models.CharField(max_length=200)
    message_subject = models.CharField(max_length=200)
    message_body = models.CharField(max_length=200)
    recepient = models.ForeignKey(User, on_delete=models.CASCADE)
    message_status = models.ForeignKey(Message_Status, on_delete=models.CASCADE)
    customer_address = models.CharField(max_length=200)
    date_sent = models.DateTimeField('date sent')
    date_received = models.DateTimeField('date received')

class Product_Type(models.Model):
    product_type = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created')


class Customer_Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_type = models.ForeignKey(Product_Type, on_delete=models.CASCADE)
    product_description = models.TextField()
    created_on= models.DateTimeField('date created')

class Product_Requirements(models.Model):
    product = models.ForeignKey(Customer_Product, on_delete=models.CASCADE)
    requirement_description = models.TextField()
    recommended_test = models.TextField()
    created_on= models.DateTimeField('date created')



