from django import forms
from reservation.models import Reservation

class ReservationForm(forms.ModelForm):

  class Meta:
    model = Reservation
    fields = [
      'nom',
      'email',
      'participation_partielle',
      'montant',
      'discret',
      'message',
    ]
  def __init__(self, foo=None, *args, **kwargs):
    super(ReservationForm, self).__init__(*args, **kwargs)