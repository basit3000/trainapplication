from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from tickets.models import Tickets
from locations.models import Locations

def home(request):
    all_tickets = Tickets.objects.all()
    all_locations = Locations.objects.all()
    return render(request, 'home/welcome.html',{'locations': all_locations, 'tickets': all_tickets})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})

