from django.db import models


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    operating_airlines = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()

    def __str__(self):
        return self.flight_number


class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flight} - {self.passenger}'
