from django.db import models
from developer.models import Developer

class Resource_Manager(models.Model):
    resource_manager = models.ForeignKey(Developer, on_delete=models.CASCADE)
    created_on= models.DateTimeField('date created')

class Resource_Type(models.Model):
    resource_type = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created')

class Resource_Status(models.Model):
    resource_status = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created')

class Resource(models.Model):
    resource_name = models.CharField(max_length=200)
    resource_manager = models.ForeignKey(Resource_Manager, on_delete=models.CASCADE)
    resource_type = models.ForeignKey(Resource_Type, on_delete=models.CASCADE)
    resource_status = models.ForeignKey(Resource_Status, on_delete=models.CASCADE)
    cost = models.FloatField()
    acquisition_date = models.DateTimeField('acquisition date')