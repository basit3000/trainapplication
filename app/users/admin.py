from django.contrib import admin

from . import models

class CustomUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.CustomUser, CustomUserAdmin)