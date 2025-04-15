from django.shortcuts import render, redirect
from .models import Locations
from django.contrib.admin.views.decorators import staff_member_required
from .forms import LocationForm

def list(request):
    all_locations = Locations.objects.all()
    return render(request, 'locations/locations_list.html', {'locations': all_locations})

@staff_member_required
def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('locations:list')  
    else:
        form = LocationForm()
    return render(request, 'locations/add_location.html', {'form': form})