from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import FooSerializer, TestingRoomSerializer, TestingRoomAvailabilitySerializer, ProfessorReservationSerializer
from .models import Foo, TestingRoom, TestingRoomAvailability, ProfessorReservation
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

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
        # getting our get parameters
        room =  request.GET['roomNum']
        building = request.GET['bldg']
        # filtering for our room
        getRoom = TestingRoom.objects.filter(bldg = building).filter(room_number = room)
        serializer = TestingRoomSerializer(getRoom, many=True)
        return Response(serializer.data)
    
class TestingRoomViewAvailabilitySet(viewsets.ModelViewSet):
    #queryset = TestingRoomAvailability.objects.filter(testing_room_id = 7)
    queryset = TestingRoomAvailability.objects.all()
    serializer_class = TestingRoomAvailabilitySerializer
    
    @action(methods=['get'], detail=False)
    def roomAvailability(self,request):
        # getting our get parameters
        id =  request.GET['id']
        # filtering for our room
        getAvailability = TestingRoomAvailability.objects.filter(testing_room_id = id)
        serializer = TestingRoomAvailabilitySerializer(getAvailability, many=True)
        return Response(serializer.data)

class ProfessorReservationSet(viewsets.ModelViewSet):
    #queryset = TestingRoomAvailability.objects.filter(testing_room_id = 7)
    queryset = ProfessorReservation.objects.all()
    serializer_class = ProfessorReservationSerializer
    
    @action(methods=['get'], detail=False)
    def myReservedRooms(self,request):
        room_set = set()
        room_arr = []
        user = request.user.id
        getReservations = ProfessorReservation.objects.filter(professor_id = user)
        serializer = ProfessorReservationSerializer(getReservations, many=True)
        for reservation in serializer.data:
            getAvailability = TestingRoomAvailability.objects.filter(id = reservation['availability_id'])
            serializer1 = TestingRoomAvailabilitySerializer(getAvailability, many=True)
            testingRoomId = serializer1.data[0]['testing_room_id']
            if testingRoomId not in room_set:
                room_set.add(testingRoomId)
        print(room_set)
        roomSerializer = None
        for i,room in enumerate(room_set):
            getRoom = TestingRoom.objects.filter(id = room)
            roomSerializer = TestingRoomSerializer(getRoom,many = True)
            room_arr.append(roomSerializer.data[0])
        print(room_arr)
        return Response(room_arr)
    
    def create(self, request):
        user = request.user.id
        data = {
            'professor_id': user,
            'availability_id': request.data['availability_id'],
            'approved': request.data['approved']
        }
        
        serializer = ProfessorReservationSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            availability = TestingRoomAvailability.objects.get(id = request.data['availability_id'])
            availability.is_booked = True
            availability.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        print("DESTROY CALLED")
        reservation = self.get_object()
        availability = reservation.room_aval
        availability.is_booked = False
        availability.save()
        reservation.delete()
        
        return Response({"message": "reservation deleted"})