from django.contrib import admin
from .models import Team

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'designation', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)
admin.site.site_header = 'Carzone Admin'