from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/welcome.html',{})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})

