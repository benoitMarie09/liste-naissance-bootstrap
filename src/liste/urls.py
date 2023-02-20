from django.urls import path
from .views import liste


urlpatterns = [
    path('', liste, name="liste"),
]
