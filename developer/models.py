from sqlite3 import IntegrityError
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.exceptions import ValidationError
from customermanagement.models import Customer_Product

class Role(models.Model):
    role_name = models.CharField(max_length=200)

class Developer_Status(models.Model):
    developer_status = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created', default=datetime.now())
    def __str__(self):
        return self.developer_status

class Developer(models.Model):
    developer_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    developer_status = models.ForeignKey(Developer_Status, on_delete=models.CASCADE, null=True)
    user_details = models.ForeignKey(User, on_delete=models.CASCADE, related_name='developer_user_details', null=True, blank=True)
    telephone = models.CharField(max_length=200)
    registration_date = models.DateTimeField('registration date', default=datetime.now())
    def __str__(self):
        return self.developer_name or ''

class Project_Phase(models.Model):
    project_phase = models.CharField(max_length=200)
    def __str__(self):
        return self.project_phase  or ''

class Project(models.Model):
    product = models.ForeignKey(Customer_Product, on_delete=models.CASCADE, related_name='product_projects', null=True, blank=True)
    project_name = models.CharField(max_length=200)
    start_date = models.DateTimeField('starting date', default=datetime.now())
    deadline = models.DateTimeField('deadline', default=datetime.now())
    project_phase = models.ForeignKey(Project_Phase, on_delete=models.CASCADE, related_name='project_phase_projects', null=True, blank=True)
    def __str__(self):
        return self.project_name
    
class Feedback(models.Model):
    product = models.ForeignKey(Customer_Product, on_delete=models.CASCADE, related_name='product_feedbacks', null=True, blank=True)
    subject = models.CharField(max_length=200)
    feedback = models.TextField()
    date_received = models.DateTimeField('date received', default=datetime.now())
    comments = models.TextField(null=True)
    added_by= models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_feedbacks', null=True, blank=True)
    def __str__(self):
        return self.feedback

    
class Sprint(models.Model):
    start_date = models.DateTimeField('start date', default=datetime.now())
    end_date = models.DateTimeField('end date', default=datetime.now())
    sprint_title = models.CharField(max_length=200, null=True)
    expected_outcome = models.TextField()
    added_by= models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_sprints', null=True, blank=True)
    def __str__(self):
        return self.sprint_title
    
class Sprint_Backlog(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name='sprint_backlogs', null=True, blank=True)
    backlog_item = models.TextField()
    added_by= models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_sprint_backlogs', null=True, blank=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    expected_outcome = models.TextField()
    def __str__(self):
        return self.backlog_item

class Backlog_allocation_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Sprint_Backlog_Allocations(models.Model):
    sprint_backlog = models.ForeignKey(Sprint_Backlog, on_delete=models.CASCADE, related_name='sprint_backlog_allocations', null=True, blank=True)
    developer= models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_sprint_backlog_allocations', null=True, blank=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    allocation_status = models.ForeignKey(Backlog_allocation_Status, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.developer.developer_name + " => " +self.sprint_backlog.expected_outcome
    
class Daily_Scrum(models.Model):
    date = models.DateTimeField('date', default=datetime.now())
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name='sprint_daily_scrums', null=True, blank=True)
    outcome = models.TextField()
    added_by= models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_daily_scrums', null=True, blank=True)
    def __str__(self):
        return self.outcome

class Review_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Sprint_Review(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name='sprint_reviews', null=True, blank=True)
    review = models.TextField()
    added_by= models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_sprint_reviews', null=True, blank=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    review_status = models.ForeignKey(Review_Status, on_delete=models.CASCADE)
    def __str__(self):
        return self.review

class Sprint_Retrospective(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name='sprint_retrospectives', null=True, blank=True)
    retrospective = models.TextField()
    added_by= models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_sprint_retrospectives', null=True, blank=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    def __str__(self):
        return self.retrospective
