from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import FooSerializer, TestingRoomSerializer, TestingRoomAvailabilitySerializer
from .models import Foo, TestingRoom, TestingRoomAvailability
from rest_framework.decorators import action
from rest_framework.response import Response

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

class FooViewSet(viewsets.ModelViewSet):
    queryset = Foo.objects.all().order_by('name')
    serializer_class = FooSerializer
    
class TestingRoomViewSet(viewsets.ModelViewSet):
    queryset = TestingRoom.objects.all()
    serializer_class = TestingRoomSerializer
    
    @action(methods=['get'], detail=False)
    def getTestingRoom(self,request):
        getUserType = TestingRoom.objects.filter(bldg = "Winston Chung Hall").filter(room_number = 234)
        serializer = TestingRoomSerializer(getUserType, many=True)
        return Response(serializer.data)
    
class TestingRoomViewAvailabilitySet(viewsets.ModelViewSet):
    #queryset = TestingRoomAvailability.objects.filter(testing_room_id = 7)
    queryset = TestingRoomAvailability.objects.all()
    serializer_class = TestingRoomAvailabilitySerializer