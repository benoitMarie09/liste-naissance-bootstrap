from django.shortcuts import render
from .models import Cadeaux

# Create your views here.
def liste(request):
  context = dict()
  cadeaux = Cadeaux.objects.all()
  context['cadeaux'] = cadeaux