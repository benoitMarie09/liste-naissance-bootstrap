from django.shortcuts import render
from .models import Cadeau

# Create your views here.
def liste(request):
  context = dict()
  cadeaux = Cadeau.objects.all()
  for cadeau in cadeaux:
    cadeau.save()
  context['cadeaux'] = cadeaux


  return render(request, "liste/index.html", context)