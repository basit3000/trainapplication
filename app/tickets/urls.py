from django.urls import path
from . import views

urlpatterns = [
    path('tickets', views.list),
    path('new', views.TicketsCreateView.as_view(), name="tickets.new"),
    path('buy_tickets/', views.buy_tickets, name='buy_tickets'),
    path('buy_tickets/<int:ticket_id>/', views.buy_tickets_with_id, name='buy_tickets_with_id'),
    path('tickets/<int:ticket_id>/delete', views.TicketsDeleteView.as_view(), name='tickets_delete'),
    path('tickets/<int:ticket_id>', views.detail),
]