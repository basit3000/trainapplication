from django.contrib import admin
from tickets.models import UserTickets
from . import models

class CustomUserAdmin(admin.ModelAdmin):
    pass

class UserTicketsInline(admin.TabularInline):
    model = UserTickets
    extra = 1

admin.site.register(models.CustomUser, CustomUserAdmin)