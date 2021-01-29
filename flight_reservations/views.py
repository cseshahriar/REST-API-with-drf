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
from rest_framework import status


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


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(
        id=request.data['flight_id']
    )

    passenger = Passenger()
    passenger.first_name = request.data['first_name']
    passenger.middle_name = request.data['middle_name']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    Reservation.save(reservation)
    return Response(status.status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
