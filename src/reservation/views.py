from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView
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

    def get_initial(self):
        initial = super(CreateReservationView, self).get_initial()
        initial = initial.copy()
        cadeau = Cadeau.objects.get(slug=self.kwargs['slug'])
        initial['cadeau'] = cadeau
        return initial

    def form_valid(self, form):
        super(CreateReservationView, self).form_valid(form)
        self.send_confirm_mail(form)
        print('------helloo------')
        return super(CreateReservationView, self).form_valid(form)

    def get_success_url(self):
        self.object.cadeau.save()
        return reverse('reservation:success', kwargs={'slug': self.object.slug})

    def send_confirm_mail(self, form):
        base_url = self.request.build_absolute_uri().split("/")[0]+"/"+self.request.build_absolute_uri(
        ).split("/")[1]+"/"+self.request.build_absolute_uri().split("/")[2]
        message = "Merci {name},\nNous sommes impatients de pouvoir profiter de ce cadeau ({cadeau}),\n Gros bisous de la part de Coline, Benoit, et le bébé.\n Pour annuler la réservation cliqué sur le lien :\n  {url}\n ".format(            
            name=form.cleaned_data.get('nom'),
            cadeau=form.cleaned_data.get('cadeau'),
            url=base_url+reverse('reservation:delete', kwargs={'slug':form.instance.slug}))

        
        send_mail(
            subject="Merci",
            message=message,
            from_email='benoitmarie@colinelamy.fr',
            recipient_list=[form.cleaned_data.get('email')],
            fail_silently=False,
        )
        send_mail(
            subject="Reservation",
            message=f"{form.cleaned_data.get('nom')} a éfféctué une réservation sur la liste de naissance pour {form.cleaned_data.get('cadeau')}",
            from_email='benoitmarie@colinelamy.fr',
            recipient_list=['benoit.marie09@proton.me','mauvelamy@gmail.com'],
            fail_silently=False,
        )


    def get_context_data(self, **kwargs):
        cadeau_slug = self.kwargs['slug']
        cadeau = Cadeau.objects.get(slug=cadeau_slug)
        kwargs['cadeau'] = cadeau
        context = super().get_context_data(**kwargs)
        return context


class ReservationDetails(DetailView):
    model = Reservation
    def get_context_data(self, **kwargs):
        reservation_slug = self.kwargs['slug']
        reservation = Reservation.objects.get(slug=reservation_slug)
        kwargs['reservation'] = reservation
        reservation.cadeau.save()
        context = super().get_context_data(**kwargs)
        return context


class ReservationDelete(DeleteView):
    model = Reservation

    def get_success_url(self):
        reservation_slug = self.kwargs['slug']
        reservation = Reservation.objects.get(slug = reservation_slug)
        cadeau = Cadeau.objects.get(reservation = reservation.pk)
        reservation.montant = 0
        cadeau.save()
        return reverse('liste:liste')