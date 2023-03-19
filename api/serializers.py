from rest_framework import serializers
from .models import Foo, TestingRoom, TestingRoomAvailability, ProfessorReservation


class FooSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foo
        fields = ('name',)
        


class TestingRoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestingRoom
        fields = ('id','room_number', 'bldg', 'capacity')
        


class TestingRoomAvailabilitySerializer(serializers.HyperlinkedModelSerializer):
    #testing_room_id = serializers.IntegerField(source="testing_room.id", read_only=True)
    testing_room_id = serializers.PrimaryKeyRelatedField(queryset=TestingRoom.objects.all(),source = "testing_room")
    class Meta:
        model = TestingRoomAvailability
        fields = ("id","testing_room_id","start_time", "end_time" ,"date", "is_booked")
        
class ProfessorReservationSerializer(serializers.HyperlinkedModelSerializer):
    professor = serializers.CharField(source="professor.username", read_only=True)
    availability_id = serializers.PrimaryKeyRelatedField(queryset=TestingRoomAvailability.objects.all(),source = "room_aval.id")
    class Meta:
        model = ProfessorReservation
        fields = ("id","availability_id", "professor", "approved")