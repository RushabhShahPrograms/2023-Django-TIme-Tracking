# 2023-Django-TIme-Tracking

Models are created as per [Time Tracking Data Dictionary](https://docs.google.com/spreadsheets/d/1od4ldcEouk1gbwi5j3DQdEWy9aycb_IQIBg_yavu_p0/edit#gid=0)

### Total Apps created
 1) userApp
 2) productApp
 
 
 ### Models.py file of productApp
 ```python
 
 from django.db import models
from userApp.models import *

class Project(models.Model):
    project_title = models.CharField(max_length=100)
    project_decription = models.TextField()
    project_technology = models.CharField(max_length=100)
    project_estimated_hours = models.IntegerField()
    project_start_date = models.DateTimeField()
    project_completion_date = models.DateTimeField()

    class Meta:
        db_table='project'
    
    def __str__ (self):
        return self.project_title

class Project_Team(models.Model):
    team_name = models.CharField(max_length=100)
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'project_team'

    def __str__(self):
        return self.team_name
    
class Status(models.Model):
    status_name = models.CharField(max_length=100)

    class Meta:
        db_table='status'
    
    def __str__(self):
        return self.status_name

class Project_Module(models.Model):
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE)
    module_name = models.CharField(max_length=100)
    module_description = models.TextField()
    module_estimated_minutes = models.IntegerField()
    module_start_date = models.DateTimeField()
    module_completion_date = models.DateTimeField()

    class Meta:
        db_table='project_module'

    def __str__(self):
        return self.module_name
    
priorityChoice=(
    ('High','High Priority'),
    ('Less','Less Priority')
)
    
class Project_Task(models.Model):
    module_id = models.ForeignKey(Project_Module,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status,on_delete=models.CASCADE)
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    priority = models.CharField(choices=priorityChoice,max_length=30)
    task_estimated_minutes = models.IntegerField()
    task_util_minutes = models.IntegerField()

    class Meta:
        db_table='project_task'

    def __str__(self):
        return self.task_title
    
class Task_Badge(models.Model):
    badge_id = models.ForeignKey(Badge,on_delete=models.CASCADE)
    task_id = models.ForeignKey(Project_Task,on_delete=models.CASCADE)
 
 ```
 
 
 ### Models.py file of userApp
 ```python
 
 from django.db import models
from django.contrib.auth.models import AbstractUser
from projectApp.models import Project_Task,Status
    
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
 
 ```
 
 ### Things added in settings.py file
 ```python
 
 import os
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = os.path.join(BASE_DIR,'static')
MEDIA_DIR = os.path.join(BASE_DIR,'media')

INSTALLED_APPS = [
    #apps added
    'userApp',
    'projectApp',
    'crispy_forms',
    'crispy_bootstrap5',
]
 
 AUTH_USER_MODEL = 'user.User'
 
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'time_tracking',
        'USER':'postgres',
        'PASSWORD':'postgres',
        'HOST':'localhost',
        'PORT':'5432'
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/static'

STATICFILES_DIRS = [
    STATIC_DIR,"static"
]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_TEMPLATE_PACK='bootstrap5'
 ```
 #### Template I selected for integration [Skydash Template](https://www.bootstrapdash.com/product/skydash-free)
 
 
 ![sky-inner](https://user-images.githubusercontent.com/90546286/224917476-2afbb876-47a1-4be1-b456-f5b75f4f10dd.jpg)
