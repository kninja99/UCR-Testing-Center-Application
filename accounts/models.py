from django.db import models
from django.contrib.auth.models import User

# Custom User models

class Student(models.Model):
    student=models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, blank = 'Student')
    
    def __str__(self):
        return self.student.username
    
class SiteAdmin(models.Model):
    site_admin=models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, blank = 'Admin')
    
    def __str__(self):
        return self.site_admin.username
    
class Professor(models.Model):
    professor=models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, blank = 'Professor')
    
    def __str__(self):
        return self.professor.username
    
class Proctor(models.Model):
    proctor=models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, blank = 'Proctor')
    
    def __str__(self):
        return self.proctor.username