from django.db import models
from serviceintegrator.models import *

# Create your models here.
class Service_Manager_Type(models.Model):
    type = models.CharField(max_length=200)

class Service_Manager_Role(models.Model):
    role = models.CharField(max_length=200)

class Service_Manager_Status(models.Model):
    status = models.CharField(max_length=200)

class Service_Manager(models.Model):
    service_integrator = models.ForeignKey(Service_Integrator, on_delete=models.CASCADE)
    service_manager_name = models.CharField(max_length=200)
    service_manager_type = models.ForeignKey(Service_Manager_Type, on_delete=models.CASCADE)
    service_manager_role = models.ForeignKey(Service_Manager_Role, on_delete=models.CASCADE)
    service_manager_status = models.ForeignKey(Service_Manager_Status, on_delete=models.CASCADE)
    current_performance = models.CharField(max_length=200)
    date_created = models.DateTimeField("date created")

class Task_Type(models.Model):
    type = models.CharField(max_length=200)

class Task_Status(models.Model):
    status = models.CharField(max_length=200)

    
class service_management_tasks(models.Model):
    service_manager = models.ForeignKey(Service_Manager, on_delete=models.CASCADE)
    task_type = models.ForeignKey(Task_Type, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    task_status = models.ForeignKey(Task_Status, on_delete=models.CASCADE)
    date_created = models.DateTimeField("date created")
