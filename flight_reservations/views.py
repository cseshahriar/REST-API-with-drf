from django.shortcuts import render
from . models import (
    Flight,
    Passenger,
    Reservation
)
from . serializers import (
    FlightSerializer,
    PassengerSerializer,
    ReservationSerializer
)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def find_flights(request):
    """ find flight """
    flights = Flight.objects.filter(
        departure_city=request.data['departure_city'],
        arrival_city=request.data['arrival_city'],
        date_of_departure=request.data['date_of_departure']
    )
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
