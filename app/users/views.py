from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser

class UserRegisterView(View):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
        return render(request, self.template_name, {'form': form})
    
@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def data(request):
    user_tickets = request.user.usertickets_set.all()
    return render(request, 'users/data.html', {'user_tickets': user_tickets})