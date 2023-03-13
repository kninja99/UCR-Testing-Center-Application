from django.contrib import admin
from .models import Foo, ProfessorReservation
from .models import TestingRoom, TestingRoomAvailability, ProfessorReservation

admin.site.register(Foo)
#admin.site.register(TestingRoom)

class TestingRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "room_number" , "bldg" , "capacity")
    
class TestingRoomAvailabilityAdmin(admin.ModelAdmin):
    list_display = ("id", "testing_room" ,"start_time" , "end_time" , "date", "is_booked")
    
class ProfessorReservationAdmin(admin.ModelAdmin):
    list_display = ("room_aval", "professor", "approved")

admin.site.register(TestingRoom, TestingRoomAdmin)
admin.site.register(TestingRoomAvailability,TestingRoomAvailabilityAdmin )
admin.site.register(ProfessorReservation,  ProfessorReservationAdmin)