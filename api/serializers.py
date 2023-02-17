from rest_framework import serializers
from .models import Foo, TestingRoom, TestingRoomAvailability


class FooSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foo
        fields = ('name',)
        


class TestingRoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestingRoom
        fields = ('id','room_number', 'bldg', 'capacity')
        


class TestingRoomAvailabilitySerializer(serializers.HyperlinkedModelSerializer):
    testing_room_id = serializers.IntegerField(source="testing_room.id", read_only=True)

    class Meta:
        model = TestingRoomAvailability
        fields = ("testing_room_id","start_time", "end_time" ,"date", "is_booked")