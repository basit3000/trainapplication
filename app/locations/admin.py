from django.contrib import admin
from . import models

class LocationsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(models.Locations, LocationsAdmin)