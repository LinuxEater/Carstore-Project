from django.contrib import admin
from django.utils.html import format_html
from .models import Team

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 50%;">'.format(object.photo.url))

    thumbnail.short_description = 'Photo'
    
    list_display = ('id','first_name', 'last_name', 'thumbnail', 'email', 'phone', 'designation', 'created_at')
    list_display_links = ('id','thumbnail','first_name',)
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)
admin.site.site_header = 'Carzone Admin'