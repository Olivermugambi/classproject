from django.db import models
from developer.models import Developer
from datetime import datetime

class Service_Pipeline(models.Model):
    name = models.CharField(max_length=200)
    pipeline_description = models.TextField(null=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    def __str__(self):
        return self.name

class Service_Pipeline_Item_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Service_Type(models.Model):
    type = models.CharField(max_length=200)
    def __str__(self):
        return self.type

class Service_Pipeline_Item(models.Model):
    pipeline = models.ForeignKey(Service_Pipeline, on_delete=models.CASCADE, related_name='pipelined_items', null=True, blank=True)
    service = models.TextField()
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    status = models.ForeignKey(Service_Pipeline_Item_Status, on_delete=models.CASCADE, null=True)
    service_type = models.ForeignKey(Service_Type, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.service
    
class Service_Integration_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Service_Integration(models.Model):
    name = models.CharField(max_length=200)
    integration_description = models.TextField(null=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    status = models.ForeignKey(Service_Integration_Status, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Service_Integrator(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    def __str__(self):
        return self.name

class Service_Integration_Item(models.Model):
    integration = models.ForeignKey(Service_Integration, on_delete=models.CASCADE, related_name='service_integration_items', null=True, blank=True)
    service = models.ForeignKey(Service_Pipeline_Item, on_delete=models.CASCADE, related_name='service_pipeline_integration_items')
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    integrator = models.ForeignKey(Service_Integrator, on_delete=models.CASCADE, related_name='service_integrator_items', null=True, blank=True)
    def __str__(self):
        if not self.service==None: 
            return self.service.service
        else:
            return ''

class Integration_Tool_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Integration_Tool_Type(models.Model):
    type = models.CharField(max_length=200)
    def __str__(self):
        return self.type

class Service_Integration_Tool(models.Model):
    tool_type = models.ForeignKey(Integration_Tool_Type, on_delete=models.CASCADE, null=True)
    tool_status = models.ForeignKey(Integration_Tool_Status, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    description = models.TextField()
    developer= models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_integration_tools', null=True, blank=True)
    def __str__(self):
        return self.description

class Tool_Allocation_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Integration_Tool_Allocation(models.Model):
    tool = models.ForeignKey(Service_Integration_Tool, on_delete=models.CASCADE, related_name='integration_tool_allocations', null=True, blank=True)
    integrator = models.ForeignKey(Service_Integrator, on_delete=models.CASCADE, related_name='service_integrator_tool_allocations', null=True, blank=True)
    allocation_status = models.ForeignKey(Tool_Allocation_Status, on_delete=models.CASCADE, null=True)
    allocation_date = models.DateTimeField('allocation date', default=datetime.now())
    manager= models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='allocated_integration_tools', null=True, blank=True)
    def __str__(self):
        if not self.tool==None: 
            return self.tool.description
        else:
            return ''

class Progress(models.Model):
    progress = models.CharField(max_length=200)
    def __str__(self):
        return self.progress

class Integration_Progress(models.Model):
    integrator = models.ForeignKey(Service_Integrator, on_delete=models.CASCADE, related_name='service_integrator_progress', null=True, blank=True)
    progress = models.ForeignKey(Progress, on_delete=models.CASCADE, null=True)
    checkpoint_date = models.DateTimeField('checkpoint date', default=datetime.now())
    def __str__(self):
        if not self.progress==None: 
            return self.progress.progress
        else:
            return ''

class Integration_Outcome(models.Model):
    integrator = models.ForeignKey(Service_Integrator, on_delete=models.CASCADE, related_name='service_integration_outcomes', null=True, blank=True)
    outcome = models.TextField()
    completion_date = models.DateTimeField('completion date', default=datetime.now())
    manager= models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_integration_outcomes', null=True, blank=True)
    def __str__(self):
        return self.outcome

class Recommended_Adaptations(models.Model):
    integrator = models.ForeignKey(Service_Integrator, on_delete=models.CASCADE, related_name='service_integrator_recommended_adaptations', null=True, blank=True)
    recommendation = models.TextField()
    date = models.DateTimeField('recommendation date', default=datetime.now())
    recommender= models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_integration_recommended_adaptations', null=True, blank=True)
    def __str__(self):
        return self.recommendation