from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .models import Reservation
from .forms import ReservationForm
from liste.models import Cadeau

# Create your views here.
class CreateReservationView(CreateView):
  model = Reservation
  form_class = ReservationForm
  template_name = 'reservation/reservation_form.html' 

  def form_valid(self, form):
    cadeau_slug = self.kwargs['slug']
    form.instance.cadeau = Cadeau.objects.get(slug = cadeau_slug)
    return super().form_valid(form)
  
  def get_success_url(self):
        return reverse('success')

class ReservationDetails(DetailView):
    model = Reservation