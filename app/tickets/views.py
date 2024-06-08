from django.shortcuts import render
from .models import Tickets

def list(request):
    all_tickets = Tickets.objects.all()
    return render(request, 'tickets/tickets_list.html', {'tickets': all_tickets})