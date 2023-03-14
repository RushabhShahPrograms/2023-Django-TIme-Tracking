from django.db import models
from django.contrib.auth.models import AbstractUser
from projectApp.models import Project_Task,Status

roleChoice= (
    ('admin','Admin'),
    ('manager','Project Manager'),
    ('leader','Team Leader'),
    ('developer','Developer')
)

class Role(models.Model):
    rolename=models.CharField(choices=roleChoice,max_length=20)

    class Meta:
        db_table='role'

    def __str__(self):
        return self.rolename
    
genderChoice=(
    ("Male","male"),
    ("Female","female")
)

class User(AbstractUser):
    is_developer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    gender = models.CharField(choices=genderChoice,max_length=30)
    joining_date = models.DateField()
    birth_date = models.DateField()

    class Meta:
        db_table='user'

    def __str__(self):
        return self.name
    
badgeChoice=(
    ('IN','InProgress'),
    ('QF','QuickFinisher'),
    ('LL','LazyLoader'),
    ('SU','SilentUser')
)
class Badge(models.Model):
    badge = models.CharField(choices=badgeChoice,max_length=25)

    class Meta:
        db_table='badge'

    def __str__(self):
        return self.badge
    
class User_Task(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    task_id = models.ForeignKey(Project_Task,on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status,on_delete=models.CASCADE)
    user_totalutil_minutes = models.IntegerField()

    class Meta:
        db_table='user_task'

    def __str__(self):
        return self.user_id,self.task_id