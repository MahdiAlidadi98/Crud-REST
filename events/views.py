# Create your views here.
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def eventList(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def eventDetail(request, pk):
    events = Event.objects.all(id=pk)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def eventCreate(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def eventUpdate(request, pk):
    event = Event.objects.all(id=pk)
    serializer = EventSerializer(instance=event, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def eventDelete(request, pk):
    event = Event.objects.all(id=pk)
    event.delete()
    return Response('Deleted')