from django.db import models
from django.contrib.auth.models import User

# Custom User models
class User(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    userTypeChoices = (("student", "student"),
    ("admin", "admin"),
    ("proctor", "proctor"),
    ("professor", "professor"))
    
    userType = models.CharField(
        max_length = 50,
        choices = userTypeChoices,
        default = 'student'
    )
    
    def __str__(self):
        return self.user.username