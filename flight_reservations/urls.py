from django.urls import path, include
from . views import (
    FlightViewSet,
    ReservationViewSet,
    PassengerViewSet,
    find_flights,
    save_reservation
)

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('flights', FlightViewSet, basename='flights')
router.register('passengers', PassengerViewSet, basename='passengers')
router.register('reservations', ReservationViewSet, basename='reservations')

urlpatterns = [
    path('find_flight/', find_flights),
    path('save_reservation/', save_reservation),
    path('', include(router.urls))
]
