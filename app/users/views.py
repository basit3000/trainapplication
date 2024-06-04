from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

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