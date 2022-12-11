from django.db import models
from developer.models import Developer

class Service_Pipeline(models.Model):
    name = models.CharField(max_length=200)
    pipeline_description = models.TextField()
    creation_date = models.DateTimeField('creation date')

class Service_Pipeline_Item_Status(models.Model):
    status = models.CharField(max_length=200)

class Service_Type(models.Model):
    type = models.CharField(max_length=200)

class Service_Pipeline_Item(models.Model):
    pipeline = models.ForeignKey(Service_Pipeline, on_delete=models.CASCADE)
    service = models.TextField()
    creation_date = models.DateTimeField('creation date')
    status = models.ForeignKey(Service_Pipeline_Item_Status, on_delete=models.CASCADE)
    service_type = models.ForeignKey(Service_Type, on_delete=models.CASCADE)
    
class Service_Integration_Status(models.Model):
    status = models.CharField(max_length=200)

class Service_Integration(models.Model):
    name = models.CharField(max_length=200)
    integration_description = models.TextField()
    creation_date = models.DateTimeField('creation date')
    status = models.ForeignKey(Service_Integration_Status, on_delete=models.CASCADE)

class Service_Integrator(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    creation_date = models.DateTimeField('creation date')

class Service_Integration_Item(models.Model):
    integration = models.ForeignKey(Service_Integration, on_delete=models.CASCADE)
    service = models.ForeignKey(Service_Pipeline_Item, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date')
    integrator = models.ForeignKey(Service_Integrator, on_delete=models.CASCADE)

class Integration_Tool_Status(models.Model):
    status = models.CharField(max_length=200)

class Integration_Tool_Type(models.Model):
    type = models.CharField(max_length=200)

class Service_Integration_Tool(models.Model):
    tool_type = models.ForeignKey(Integration_Tool_Type, on_delete=models.CASCADE)
    tool_status = models.ForeignKey(Integration_Tool_Status, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date')
    description = models.TextField()
    developer= models.ForeignKey(Developer, on_delete=models.CASCADE)

class Tool_Allocation_Status(models.Model):
    status = models.CharField(max_length=200)

class Integration_Tool_Allocation(models.Model):
    tool = models.ForeignKey(Service_Integration_Tool, on_delete=models.CASCADE)
    integrator = models.ForeignKey(Service_Integrator, on_delete=models.CASCADE)
    allocation_status = models.ForeignKey(Tool_Allocation_Status, on_delete=models.CASCADE)
    allocation_date = models.DateTimeField('allocation date')
    manager= models.ForeignKey(Developer, on_delete=models.CASCADE)

class Progress(models.Model):
    progress = models.CharField(max_length=200)

class Integration_Progress(models.Model):
    integrator = models.ForeignKey(Service_Integrator, on_delete=models.CASCADE)
    progress = models.ForeignKey(Progress, on_delete=models.CASCADE)
    checkpoint_date = models.DateTimeField('checkpoint date')

class Integration_Outcome(models.Model):
    integrator = models.ForeignKey(Service_Integrator, on_delete=models.CASCADE)
    outcome = models.TextField()
    completion_date = models.DateTimeField('completion date')
    manager= models.ForeignKey(Developer, on_delete=models.CASCADE)

class Recommended_Adaptations(models.Model):
    integrator = models.ForeignKey(Service_Integrator, on_delete=models.CASCADE)
    recommendation = models.TextField()
    date = models.DateTimeField('recommendation date')
    recommender= models.ForeignKey(Developer, on_delete=models.CASCADE)