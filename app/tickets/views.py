from django.shortcuts import render
from .models import Tickets
from django.views.generic import CreateView

def list(request):
    all_tickets = Tickets.objects.all()
    return render(request, 'tickets/tickets_list.html', {'tickets': all_tickets})

class TicketsCreateView(CreateView):
    model = Tickets
    fields = ['name','text']
    success_url = "/tickets/tickets"