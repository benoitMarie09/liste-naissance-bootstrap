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

    widgets = {
      'cadeau' : forms.HiddenInput()
    }

    labels = {
      'nom' : 'Nom :',
      'email': 'Adresse mail :',
      'participation_partielle' : 'Je souhaite participer partiellement',
      'montant' : 'Montant :',
      'discret' : 'Je ne souhaite pas que mon nom apparaisse dans la liste des cadeaux',
      'message' : 'Un petit message pour Coline et Benoit'
    }
    help_texts = {
      'email' : 'Vous recevrez un email de confirmation avec un lien pour annuler la reservasion',
    }
  def __init__(self, *args, **kwargs):
    super(ReservationForm, self).__init__(*args, **kwargs)
    montant_restant = kwargs['initial']['cadeau'].montant_restant
    self.fields['montant'].widget.attrs.update(
            {'max': montant_restant, 'step':0.1})
    self.fields['montant'].help_text = f'montant max : {montant_restant}€'
    if self.fields['participation_partielle'] == False:
      self.fields['montant'].widget = forms.HiddenInput()