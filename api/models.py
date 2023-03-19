from django.db import models
from django.contrib.auth.models import User

class Foo(models.Model):
  name = models.CharField(max_length=60)

  def __str__(self):
    return self.name
  
# testing room model
class TestingRoom(models.Model):
  room_number = models.IntegerField()
  bldg = models.CharField(max_length=100)
  capacity = models.IntegerField()
  
  class Meta:
    unique_together = ('room_number','bldg')
  
  def __str__(self):
    return str(self.room_number)
  
class TestingRoomAvailability(models.Model):
  testing_room = models.ForeignKey(TestingRoom, on_delete=models.CASCADE)
  start_time = models.TimeField()
  end_time = models.TimeField()
  date = models.DateField()
  # possibly can changes this to a int feild later if we want to 
  # allow for multipul professors book a time/date
  is_booked = models.BooleanField(default=False)
  # possibly add a foreign key that will allow us to reference
  # the professors id so we can notify classes 
  class Meta:
    unique_together = ('testing_room','start_time','end_time','date')
    
  def __str__(self):
    return f"{str(self.testing_room)} {str(self.date)} ({str(self.start_time)} - {str(self.end_time)})"

class ProfessorReservation(models.Model):
  room_aval = models.ForeignKey(TestingRoomAvailability, on_delete=models.CASCADE,unique=True)
  professor = models.ForeignKey(User,on_delete=models.CASCADE)
  approved = models.BooleanField(default=True)