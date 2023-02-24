from django.urls import path
from .views import CreateReservationView, ReservationDetails, ReservationDelete

app_name = 'reservation'
urlpatterns = [
    path('<slug:slug>/', CreateReservationView.as_view(), name="reservation"),
    path('success/<slug:slug>/',ReservationDetails.as_view() ,name='success'),
    path('delete/<slug:slug>/',ReservationDelete.as_view(), name='delete')
]
