from django.contrib import admin
from . import models

class UserTicketsAdmin(admin.ModelAdmin):
    list_display = ('user', 'ticket', 'issue_date', 'expiry_date')

class UserTicketInline(admin.TabularInline):
    model = models.UserTickets
    extra = 1
    
class TicketsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [UserTicketInline]

admin.site.register(models.Tickets, TicketsAdmin)
admin.site.register(models.UserTickets, UserTicketsAdmin)