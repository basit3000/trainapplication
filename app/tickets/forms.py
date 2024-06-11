from django import forms
from .models import Tickets, UserTickets

class BuyTicketsForm(forms.ModelForm):
    ticket = forms.ModelChoiceField(queryset=Tickets.objects.all(), empty_label="Select Ticket")
    #issue_date = forms.DateField(widget=forms.SelectDateWidget)
    #expiry_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = UserTickets
        fields = ['ticket',]