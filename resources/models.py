from django.db import models
from developer.models import Developer
from datetime import datetime

class Resource_Manager(models.Model):
    resource_manager = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_resource_management', null=True, blank=True)
    created_on= models.DateTimeField('date created', default=datetime.now())
    def __str__(self):
        return self.resource_manager.developer_name

class Resource_Type(models.Model):
    resource_type = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created', default=datetime.now())
    def __str__(self):
        return self.resource_type

class Resource_Status(models.Model):
    resource_status = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created', default=datetime.now())
    def __str__(self):
        return self.resource_status

class Resource(models.Model):
    resource_name = models.CharField(max_length=200)
    resource_manager = models.ForeignKey(Resource_Manager, on_delete=models.CASCADE, related_name='resources_managed', null=True, blank=True)
    resource_type = models.ForeignKey(Resource_Type, on_delete=models.CASCADE, null=True)
    resource_status = models.ForeignKey(Resource_Status, on_delete=models.CASCADE, null=True)
    cost = models.FloatField(null=True)
    acquisition_date = models.DateTimeField('acquisition date', default=datetime.now())
    def __str__(self):
        return self.resource_name or ''