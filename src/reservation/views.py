from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .models import Reservation
from .forms import ReservationForm
from liste.models import Cadeau
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
class CreateReservationView(CreateView):
  model = Reservation
  form_class = ReservationForm
  template_name = 'reservation/reservation_form.html' 

  def form_valid(self, form):
    message = "{name} / {email} said: ".format(
        name=form.cleaned_data.get('nom'),
        email=form.cleaned_data.get('email'))
    message += "\n\n{0}".format(form.cleaned_data.get('message'))
    send_mail(
        subject="coucou",
        message=message,
        from_email='benoitmarie@colinelamy.fr',
        recipient_list=[form.cleaned_data.get('email')],
    )
    cadeau_slug = self.kwargs['slug']
    form.instance.cadeau = Cadeau.objects.get(slug = cadeau_slug)
    return super(CreateReservationView, self).form_valid(form)
  
  def get_success_url(self):
        return reverse('success', kwargs={'pk': self.object.pk})

class ReservationDetails(DetailView):
    model = Reservation