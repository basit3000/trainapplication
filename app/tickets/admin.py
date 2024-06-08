from django.contrib import admin
from . import models

class TicketsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(models.Tickets, TicketsAdmin)