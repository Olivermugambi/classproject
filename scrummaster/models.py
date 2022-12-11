from django.db import models
from customermanagement.models import Customer_Product, Customer_Profile
from developer.models import Developer

class Contact_Person_Status(models.Model):
    status = models.CharField(max_length=200)
    created_on= models.DateTimeField('date created')

class Contact_Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    status = models.ForeignKey(Contact_Person_Status, on_delete=models.CASCADE)
    registration_date = models.DateTimeField('registration date')

class Customer(models.Model):
    customer_details = models.ForeignKey(Customer_Profile, on_delete=models.CASCADE)
    registration_date = models.DateTimeField('registration date')
    contact_person = models.ForeignKey(Contact_Person, on_delete=models.CASCADE)

class Project_Phase(models.Model):
    project_phase = models.CharField(max_length=200)

class Project_Manager(models.Model):
    project_manager = models.ForeignKey(Developer, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date')

class Project(models.Model):
    product = models.ForeignKey(Customer_Product, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    start_date = models.DateTimeField('starting date')
    deadline = models.DateTimeField('deadline')
    project_phase = models.ForeignKey(Project_Phase, on_delete=models.CASCADE)
    project_manager = models.ForeignKey(Project_Manager, on_delete=models.CASCADE)
    
class Feedback(models.Model):
    product = models.ForeignKey(Customer_Product, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    feedback = models.TextField()
    date_received = models.DateTimeField('date received')
    comments = models.TextField()

class Feedback_Status(models.Model):
    status = models.CharField(max_length=200)

class Feedback_Recepient(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    recepient = models.ForeignKey(Developer, on_delete=models.CASCADE)
    status = models.ForeignKey(Feedback_Status, on_delete=models.CASCADE)

class Priority(models.Model):
    priority = models.CharField(max_length=200)

class Plan_Status(models.Model):
    status = models.CharField(max_length=200)

class Project_Plan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    plan = models.TextField()
    deliverable = models.TextField()
    deadline = models.DateTimeField('deadline')
    plan_priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    plan_manager = models.ForeignKey(Project_Manager, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date')
    plan_status= models.ForeignKey(Plan_Status, on_delete=models.CASCADE)

class Risk_Status(models.Model):
    status = models.CharField(max_length=200)

class Project_Plan_Risk(models.Model):
    project_plan = models.ForeignKey(Project_Plan, on_delete=models.CASCADE)
    risk = models.TextField()
    risk_priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    risk_manager = models.ForeignKey(Project_Manager, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date')
    risk_status= models.ForeignKey(Risk_Status, on_delete=models.CASCADE)

class Development_Status(models.Model):
    status = models.CharField(max_length=200)

class Project_Development(models.Model):
    development_plan = models.ForeignKey(Project_Plan, on_delete=models.CASCADE)
    scrum_master = models.ForeignKey(Developer, on_delete=models.CASCADE)
    required_skills = models.TextField()
    deadline = models.DateTimeField('deadline')
    creation_date = models.DateTimeField('creation date')
    development_status= models.ForeignKey(Plan_Status, on_delete=models.CASCADE)

class Team_Member_Role(models.Model):
    role = models.CharField(max_length=200)

class Development_Team_Status(models.Model):
    status = models.CharField(max_length=200)

class Development_Team(models.Model):
    project_development = models.ForeignKey(Project_Development, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('creation date')
    team_status= models.ForeignKey(Development_Team_Status, on_delete=models.CASCADE)

class Team_Member_Status(models.Model):
    status = models.CharField(max_length=200)

class Team_Member(models.Model):
    team = models.ForeignKey(Development_Team, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    member_role = models.ForeignKey(Team_Member_Role, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date')
    member_status= models.ForeignKey(Team_Member_Status, on_delete=models.CASCADE)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')

class Development_Rule(models.Model):
    project_development = models.ForeignKey(Project_Development, on_delete=models.CASCADE)
    rule = models.CharField(max_length=200)
    justification = models.TextField()
    creation_date = models.DateTimeField('creation date')
    made_by= models.ForeignKey(Project_Manager, on_delete=models.CASCADE)

class Development_Rule_Feedback(models.Model):
    rule = models.ForeignKey(Development_Rule, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    feedback = models.TextField()
    creation_date = models.DateTimeField('creation date')
    
class Release_Status(models.Model):
    status = models.CharField(max_length=200)

class Release_Strategy(models.Model):
    strategy = models.TextField()
    manager= models.ForeignKey(Project_Manager, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date')

class Release_Backlog(models.Model):
    backlog = models.TextField()
    manager= models.ForeignKey(Project_Manager, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date')

class Product_Release(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    release_strategy = models.ForeignKey(Release_Strategy, on_delete=models.CASCADE)
    release_backlog = models.ForeignKey(Release_Backlog, on_delete=models.CASCADE)
    release_definition = models.TextField()
    release_date = models.DateTimeField('release date')
    release_status= models.ForeignKey(Release_Status, on_delete=models.CASCADE) 

class Release_Feature(models.Model):
    feature = models.TextField()
    release= models.ForeignKey(Product_Release, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    release_date = models.DateTimeField('feature release date') 