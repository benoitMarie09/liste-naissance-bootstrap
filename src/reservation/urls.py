from django.urls import path
from .views import CreateReservationView, ReservationDetails


urlpatterns = [
    path('<slug:slug>/', CreateReservationView.as_view(), name="reservation"),
    path('success',ReservationDetails.as_view() ,name='success')
]
