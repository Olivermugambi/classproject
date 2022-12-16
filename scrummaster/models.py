from django.db import models
from customermanagement.models import Customer_Product, Customer_Profile
from developer.models import Developer
from datetime import datetime

class Contact_Person_Status(models.Model):
    status = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created', default=datetime.now())
    def __str__(self):
        return self.status

class Contact_Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    status = models.ForeignKey(Contact_Person_Status, on_delete=models.CASCADE, null=True)
    registration_date = models.DateTimeField('registration date', default=datetime.now())
    customer = models.ForeignKey(Customer_Profile, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Project_Phase(models.Model):
    project_phase = models.CharField(max_length=200)
    def __str__(self):
        return self.project_phase

class Project(models.Model):
    product = models.ForeignKey(Customer_Product, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    start_date = models.DateTimeField('starting date', default=datetime.now())
    deadline = models.DateTimeField('deadline', default=datetime.now())
    project_phase = models.ForeignKey(Project_Phase, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.project_name

class Project_Manager(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    project_manager = models.ForeignKey(Developer, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    def __str__(self):
        return self.project_manager.developer_name
    
class Feedback(models.Model):
    product = models.ForeignKey(Customer_Product, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    feedback = models.TextField()
    date_received = models.DateTimeField('date received', default=datetime.now())
    comments = models.TextField(null=True)
    def __str__(self):
        return self.feedback

class Priority(models.Model):
    priority = models.CharField(max_length=200)
    def __str__(self):
        return self.priority

class Plan_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Project_Plan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    plan = models.TextField()
    deliverable = models.TextField(null=True)
    deadline = models.DateTimeField('deadline', default=datetime.now())
    plan_priority = models.ForeignKey(Priority, on_delete=models.CASCADE, null=True)
    plan_manager = models.ForeignKey(Project_Manager, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    plan_status= models.ForeignKey(Plan_Status, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.plan

class Risk_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Project_Plan_Risk(models.Model):
    project_plan = models.ForeignKey(Project_Plan, on_delete=models.CASCADE)
    risk = models.TextField()
    risk_priority = models.ForeignKey(Priority, on_delete=models.CASCADE, null=True)
    risk_manager = models.ForeignKey(Project_Manager, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    risk_status= models.ForeignKey(Risk_Status, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.risk

class Development_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Project_Development(models.Model):
    development_plan = models.ForeignKey(Project_Plan, on_delete=models.CASCADE)
    scrum_master = models.ForeignKey(Project_Manager, on_delete=models.CASCADE)
    required_skills = models.TextField(null=True)
    deadline = models.DateTimeField('deadline', default=datetime.now())
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    development_status= models.ForeignKey(Development_Status, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.development_plan.plan

class Team_Member_Role(models.Model):
    role = models.CharField(max_length=200)
    def __str__(self):
        return self.role

class Development_Team_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Development_Team(models.Model):
    project_development = models.ForeignKey(Project_Development, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    team_status= models.ForeignKey(Development_Team_Status, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.team_name

class Team_Member_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Team_Member(models.Model):
    team = models.ForeignKey(Development_Team, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    member_role = models.ForeignKey(Team_Member_Role, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    member_status= models.ForeignKey(Team_Member_Status, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField('start date', default=datetime.now())
    end_date = models.DateTimeField('end date', default=datetime.now())
    def __str__(self):
        return self.developer.developer_name

class Development_Rule(models.Model):
    project_development = models.ForeignKey(Project_Development, on_delete=models.CASCADE)
    rule = models.CharField(max_length=200)
    justification = models.TextField(null=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    made_by= models.ForeignKey(Project_Manager, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.rule

class Development_Rule_Feedback(models.Model):
    rule = models.ForeignKey(Development_Rule, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    feedback = models.TextField()
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    def __str__(self):
        return self.feedback
    
class Release_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Product_Release(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    release_definition = models.TextField()
    release_date = models.DateTimeField('release date', default=datetime.now())
    release_status= models.ForeignKey(Release_Status, on_delete=models.CASCADE, null=True) 
    def __str__(self):
        return self.release_definition

class Release_Feature(models.Model):
    feature = models.TextField()
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, null=True)
    release_date = models.DateTimeField('feature release date', default=datetime.now())
    release = models.ForeignKey(Product_Release, on_delete=models.CASCADE, null=True) 
    def __str__(self):
        return self.feature

class Release_Strategy(models.Model):
    release = models.ForeignKey(Product_Release, on_delete=models.CASCADE, null=True)
    feature = models.ForeignKey(Release_Feature, on_delete=models.CASCADE, null=True)
    strategy = models.TextField()
    manager= models.ForeignKey(Project_Manager, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    def __str__(self):
        return self.strategy

class Release_Backlog(models.Model):
    backlog = models.TextField()
    manager= models.ForeignKey(Project_Manager, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    strategy = models.ForeignKey(Release_Strategy, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.backlog