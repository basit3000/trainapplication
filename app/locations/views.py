from django.shortcuts import render
from .models import Locations

def list(request):
    all_locations = Locations.objects.all()
    return render(request, 'locations/locations_list.html', {'locations': all_locations})