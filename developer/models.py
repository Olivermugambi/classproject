from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Role(models.Model):
    role_name = models.CharField(max_length=200)

class Developer_Status(models.Model):
    developer_status = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created', default=datetime.now())

class Developer(models.Model):
    developer_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    developer_status = models.ForeignKey(Developer_Status, on_delete=models.CASCADE, null=True)
    user_details = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    telephone = models.CharField(max_length=200)
    registration_date = models.DateTimeField('registration date', default=datetime.now())
    
class Sprint(models.Model):
    start_date = models.DateTimeField('start date', default=datetime.now())
    end_date = models.DateTimeField('end date', default=datetime.now())
    expected_outcome = models.TextField()
    added_by= models.ForeignKey(Developer, on_delete=models.CASCADE, null=True)
    
class Sprint_Backlog(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    backlog_item = models.TextField()
    added_by= models.ForeignKey(Developer, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    expected_outcome = models.TextField()

class Backlog_allocation_Status(models.Model):
    status = models.CharField(max_length=200)

class Sprint_Backlog_Allocations(models.Model):
    sprint_backlog = models.ForeignKey(Sprint_Backlog, on_delete=models.CASCADE)
    developer= models.ForeignKey(Developer, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    allocation_status = models.ForeignKey(Backlog_allocation_Status, on_delete=models.CASCADE)
    
class Daily_Scrum(models.Model):
    date = models.DateTimeField('date', default=datetime.now())
    sprint_backlog = models.ForeignKey(Sprint_Backlog, on_delete=models.CASCADE)
    outcome = models.TextField()

class Review_Status(models.Model):
    status = models.CharField(max_length=200)

class Sprint_Review(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    review = models.TextField()
    developer= models.ForeignKey(Developer, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    review_status = models.ForeignKey(Review_Status, on_delete=models.CASCADE)

class Sprint_Retrospective(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    retrospective = models.TextField()
    added_by= models.ForeignKey(Developer, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
