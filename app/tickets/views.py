from django.shortcuts import render, redirect, get_object_or_404
from .models import Tickets, UserTickets
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import BuyTicketsForm
from django.utils.timezone import now
from datetime import timedelta
from django.utils import timezone
from django.views.generic.edit import DeleteView
from django.http import Http404

class TicketsDeleteView(DeleteView):
    model = Tickets
    success_url = 'tickets/tickets_success.html'

def detail(request, ticket_id):
    try:
        tickets = Tickets.objects.get(pk=ticket_id)
    except Tickets.DoesNotExist:
        raise Http404("Ticket doesn't exist")
    return render(request, "tickets/tickets_detail.html", {'tickets': tickets})

def list(request):
    all_tickets = Tickets.objects.all()
    return render(request, 'tickets/tickets_list.html', {'tickets': all_tickets})

class TicketsCreateView(CreateView):
    model = Tickets
    fields = ['name','text']
    success_url = "/tickets/tickets"

@login_required
def buy_tickets(request):
    if request.method == 'POST':
        form = BuyTicketsForm(request.POST)
        if form.is_valid():
            ticket = form.cleaned_data['ticket']
            return redirect('buy_tickets_with_id', ticket_id=ticket.id)
    else:
        form = BuyTicketsForm()
    return render(request, 'tickets/tickets_buy.html', {'form': form})

@login_required
def buy_tickets_with_id(request, ticket_id):
    ticket = get_object_or_404(Tickets, pk=ticket_id)
    user = request.user
    active_tickets = UserTickets.objects.filter(user=user, ticket=ticket, expiry_date__gt=timezone.now().date())
    if active_tickets.exists():
        return render(request, 'tickets/error_page.html', {'message': 'You already have an active ticket of this type.'})
    issue_date = timezone.now().date()
    expiry_date = issue_date + timedelta(days=ticket.duration)
    user_ticket = UserTickets.objects.create(
        user=user,
        ticket=ticket,
        issue_date=issue_date,
        expiry_date=expiry_date
    )
    return render(request, 'tickets/tickets_success.html', {'message': 'You have successfully bought', 'ticket': user_ticket.ticket.name})

