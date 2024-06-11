from django.shortcuts import render, redirect
from .models import Tickets, UserTickets
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import BuyTicketsForm
from django.utils.timezone import now
from datetime import timedelta


def list(request):
    all_tickets = Tickets.objects.all()
    return render(request, 'tickets/tickets_list.html', {'tickets': all_tickets})

class TicketsCreateView(CreateView):
    model = Tickets
    fields = ['name','text']
    success_url = "/tickets/tickets"

@login_required
def buy_ticket(request):
    if request.method == 'POST':
        form = BuyTicketsForm(request.POST)
        if form.is_valid():
            user_ticket = form.save(commit=False)
            user_ticket.user = request.user
            user_ticket.issue_date = now().date()
            user_ticket.expiry_date = user_ticket.issue_date + timedelta(days=user_ticket.ticket.duration)  
            user_ticket.save()
            return redirect('profile')  
    else:
        form = BuyTicketsForm()
    return render(request, 'tickets/tickets_buy.html', {'form': form})