from django.db import models
from developer.models import *
from datetime import datetime

class Project_Manager(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_managers', null=True, blank=True)
    project_manager = models.ForeignKey(Developer, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    def __str__(self):
        return self.project_manager.developer_name

class Priority(models.Model):
    priority = models.CharField(max_length=200)
    def __str__(self):
        return self.priority

class Plan_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Project_Plan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_plans', null=True, blank=True)
    plan = models.TextField()
    deliverable = models.TextField(null=True)
    deadline = models.DateTimeField('deadline', default=datetime.now())
    plan_priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='priority_project_plans', null=True, blank=True)
    plan_manager = models.ForeignKey(Project_Manager, on_delete=models.CASCADE, related_name='manager_project_plans', null=True, blank=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    plan_status= models.ForeignKey(Plan_Status, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.plan

class Risk_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Project_Plan_Risk(models.Model):
    project_plan = models.ForeignKey(Project_Plan, on_delete=models.CASCADE, related_name='project_plan_risks', null=True, blank=True)
    risk = models.TextField()
    risk_priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='priority_project_plan_risks', null=True, blank=True)
    risk_manager = models.ForeignKey(Project_Manager, on_delete=models.CASCADE, related_name='manager_project_plan_risks', null=True, blank=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    risk_status= models.ForeignKey(Risk_Status, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.risk

class Development_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Project_Development(models.Model):
    development_plan = models.ForeignKey(Project_Plan, on_delete=models.CASCADE, related_name='dev_plan_implementations', null=True, blank=True)
    scrum_master = models.ForeignKey(Project_Manager, on_delete=models.CASCADE, related_name='scrummaster_project_developments', null=True, blank=True)
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
    project_development = models.ForeignKey(Project_Development, on_delete=models.CASCADE, related_name='dev_teams', null=True, blank=True)
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
    team = models.ForeignKey(Development_Team, on_delete=models.CASCADE, related_name='team_members', null=True, blank=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_team_memberships', null=True, blank=True)
    member_role = models.ForeignKey(Team_Member_Role, on_delete=models.CASCADE, related_name='role_team_members', null=True, blank=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    member_status= models.ForeignKey(Team_Member_Status, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField('start date', default=datetime.now())
    end_date = models.DateTimeField('end date', default=datetime.now())
    def __str__(self):
        return self.developer.developer_name

class Development_Rule(models.Model):
    project_development = models.ForeignKey(Project_Development, on_delete=models.CASCADE, related_name='project_dev_rules', null=True, blank=True)
    rule = models.CharField(max_length=200)
    justification = models.TextField(null=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    added_by= models.ForeignKey(Project_Manager, on_delete=models.CASCADE, related_name='developer_dev_rules', null=True, blank=True)
    def __str__(self):
        return self.rule

class Development_Rule_Feedback(models.Model):
    rule = models.ForeignKey(Development_Rule, on_delete=models.CASCADE, related_name='dev_rule_feedbacks', null=True, blank=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='developer_dev_rule_feedbacks', null=True, blank=True)
    feedback = models.TextField()
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    def __str__(self):
        return self.feedback
    
class Release_Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Product_Release(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_product_releases', null=True, blank=True)
    release_definition = models.TextField()
    release_date = models.DateTimeField('release date', default=datetime.now())
    release_status= models.ForeignKey(Release_Status, on_delete=models.CASCADE, null=True) 
    def __str__(self):
        return self.release_definition

class Release_Feature(models.Model):
    feature = models.TextField()
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='priority_release_features', null=True, blank=True)
    release_date = models.DateTimeField('feature release date', default=datetime.now())
    release = models.ForeignKey(Product_Release, on_delete=models.CASCADE, related_name='release_features', null=True, blank=True) 
    def __str__(self):
        return self.feature

class Release_Strategy(models.Model):
    release = models.ForeignKey(Product_Release, on_delete=models.CASCADE, related_name='release_strategies', null=True, blank=True)
    feature = models.ForeignKey(Release_Feature, on_delete=models.CASCADE, related_name='feature_release_strategies', null=True, blank=True)
    strategy = models.TextField()
    manager= models.ForeignKey(Project_Manager, on_delete=models.CASCADE, related_name='manager_release_strategies', null=True, blank=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    def __str__(self):
        return self.strategy

class Release_Backlog(models.Model):
    backlog = models.TextField()
    manager= models.ForeignKey(Project_Manager, on_delete=models.CASCADE, related_name='manager_release_backlogs', null=True, blank=True)
    creation_date = models.DateTimeField('creation date', default=datetime.now())
    strategy = models.ForeignKey(Release_Strategy, on_delete=models.CASCADE, related_name='strategy_release_backlogs', null=True, blank=True)
    def __str__(self):
        return self.backlog