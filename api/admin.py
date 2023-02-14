from django.contrib import admin
from .models import Foo
from .models import TestingRoom, TestingRoomAvailability

admin.site.register(Foo)
#admin.site.register(TestingRoom)

class TestingRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "room_number" , "bldg" , "capacity")
    
class TestingRoomAvailabilityAdmin(admin.ModelAdmin):
    list_display = ("id", "testing_room" ,"start_time" , "end_time" , "date", "is_booked")

admin.site.register(TestingRoom, TestingRoomAdmin)
admin.site.register(TestingRoomAvailability,TestingRoomAvailabilityAdmin )