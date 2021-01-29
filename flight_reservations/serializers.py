from rest_framework import serializers
from . models import (
    Flight,
    Passenger,
    Reservation
)
import re


def isFlightNumberValid(flight_number):
    print("is_flight_number_valid")


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        """ second level priority """
        validators = [isFlightNumberValid]

    def validate_flight_number(self, flight_number):
        """ first level priority """
        if(re.match("^[a-zA-Z0-9]*$", flight_number) == None):
            raise serializers.ValidationError(
                "Invalid flight number. make sure alpha numeric")
        return flight_number

    def validate(self, data):
        """ third level priority """
        print(data)
        return data


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
