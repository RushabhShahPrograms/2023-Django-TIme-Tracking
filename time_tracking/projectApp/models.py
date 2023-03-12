from django.db import models
from userApp.models import *

class Project(models.Model):
    project_title=models.CharField(max_length=100)
    project_decription=models.TextField()
    project_technology=models.CharField(max_length=100)
    project_estimated_hours=models.IntegerField()
    project_start_date=models.DateTimeField()
    project_completion_date=models.DateTimeField()

    class Meta:
        db_table='project'
    
    def __str__ (self):
        return self.project_title

class Project_Team(models.Model):
    team_name=models.CharField(max_length=100)
    project_id=models.ForeignKey(Project,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'project_team'

    def __str__(self):
        return self.team_name
    
class Status(models.Model):
    status_name=models.CharField(max_length=100)

    class Meta:
        db_table='status'
    
    def __str__(self):
        return self.status_name

class Project_Module(models.Model):
    project_id=models.ForeignKey(Project,on_delete=models.CASCADE)
    module_name=models.CharField(max_length=100)
    module_description=models.TextField()
    module_estimated_minutes=models.IntegerField()
    module_start_date=models.DateTimeField()
    module_completion_date=models.DateTimeField()

    class Meta:
        db_table='project_module'

    def __str__(self):
        return self.module_name
    
priorityChoice=(
    ('High','High Priority'),
    ('Less','Less Priority')
)
    
class Project_Task(models.Model):
    module_id=models.ForeignKey(Project_Module,on_delete=models.CASCADE)
    project_id=models.ForeignKey(Project,on_delete=models.CASCADE)
    status_id=models.ForeignKey(Status,on_delete=models.CASCADE)
    task_title=models.CharField(max_length=100)
    task_description=models.TextField()
    priority=models.CharField(choices=priorityChoice,max_length=30)
    task_estimated_minutes=models.IntegerField()
    task_util_minutes=models.IntegerField()

    class Meta:
        db_table='project_task'

    def __str__(self):
        return self.task_title
    
class Task_Badge(models.Model):
    badge_id=models.ForeignKey(Badge,on_delete=models.CASCADE)
    task_id=models.ForeignKey(Project_Task,on_delete=models.CASCADE)