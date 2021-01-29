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


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = PassengerSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = ReservationSerializer
