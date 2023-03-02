from django import forms
from reservation.models import Reservation
from liste.models import Cadeau
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Field, Button, Row, Column
from crispy_forms.bootstrap import PrependedAppendedText, PrependedText, FormActions
from django.core.exceptions import ValidationError

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
            'cadeau': forms.HiddenInput()
        }

        labels = {
            'nom': 'Nom :',
            'montant' : 'Montant :',
            'email': 'Adresse mail :',
            'participation_partielle': 'Je souhaite participer partiellement',
            'discret': 'Je ne souhaite pas que mon nom apparaisse dans la liste des cadeaux',
            'message': 'Un petit message pour Coline et Benoit'
        }
        help_texts = {
            'email': 'Vous recevrez un email de confirmation avec un lien pour annuler la reservasion',
        }

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.cadeau = kwargs['initial']['cadeau']
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('cadeau'),
            Row(
              Column(Field('participation_partielle', onchange='toggleMontant(event)'), css_class="form-group col-5 col-md-5 col-lg-5 col-xl-4 mb-0 align-self-center"),
              Column(PrependedAppendedText('montant', f'max {self.montant_restant}','€', placeholder="montant", css_id="montant", max=self.montant_restant, step=0.01),css_class="form-group col-7 col-md-7 col-lg-5 col-xl-4 mb-0 align-self-center"),
              css_class='form-row'
            ),
            'nom',
            'discret',
            'email',
            'message',
            FormActions(
                Submit('submit', 'Reserver'),
                Button('cancel', 'Annuler', onClick=f"location.href='{ reverse('liste:liste')}'")
            )
            
        )
    @property
    def montant_restant(self):
            return self.cadeau.montant_restant
    
    
    def clean_montant(self):
      value = self.cleaned_data['montant']
      if self.montant_restant <= 0:
          raise ValidationError(
              'Le cadeau a déjà été réservé',
          )
      if value > self.montant_restant:
          raise ValidationError(
              f"Le montant doit être inférieur au montant max : {self.montant_restant}",
          )
      return value