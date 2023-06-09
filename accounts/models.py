from django.db import models
from django.contrib.auth.models import User

# Custom User models
class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name="user_info")
    userTypeChoices = (("student", "student"),
    ("admin", "admin"),
    ("proctor", "proctor"),
    ("professor", "professor"))
    
    user_type = models.CharField(
        max_length = 50,
        choices = userTypeChoices,
        default = 'student'
    )
    
    def __str__(self):
        return (self.user.username)
    
    def getUserType(self):
        return self.userType
    