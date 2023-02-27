from django import forms
from reservation.models import Reservation
from liste.models import Cadeau

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
      'cadeau',
    ]
    labels = {
      'nom' : 'Nom :',
      'email': 'Adresse mail :',
      'participation_partielle' : 'Je souhaite participer partiellement',
      'montant' : 'Montant :',
      'discret' : 'Je ne souhaite pas que mon nom apparaisse dans la liste des cadeaux',
      'message' : 'Un petit message pour Coline et Benoit'
    }
    help_texts = {
      'nom' : 'coucou',
    }
  def __init__(self, *args, **kwargs):
    super(ReservationForm, self).__init__(*args, **kwargs)
    print(kwargs['initial']['cadeau'].montant_restant)
  
  