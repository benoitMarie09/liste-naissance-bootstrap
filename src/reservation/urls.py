from django.urls import path
from .views import reservation


urlpatterns = [
    path('<slug:slug>/', reservation, name="reservation"),
]
