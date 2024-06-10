from django.urls import path
from . import views

urlpatterns = [
    path('tickets', views.list),
    path('tickets/new', views.TicketsCreateView.as_view(), name="tickets.new")
]