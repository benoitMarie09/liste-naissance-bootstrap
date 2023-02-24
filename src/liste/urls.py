from django.urls import path
from .views import liste

app_name = 'liste'
urlpatterns = [
    path('', liste, name="liste"),
]
