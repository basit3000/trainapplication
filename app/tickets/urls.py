from django.urls import path
from . import views

urlpatterns = [
    path('tickets', views.list),
    path('new', views.TicketsCreateView.as_view(), name="tickets.new"),
    path('buy_tickets', views.buy_ticket, name='buy.tickets'),
]