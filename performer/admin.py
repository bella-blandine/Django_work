from django.contrib import admin
from .models import Performer

class PerformerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  

admin.site.register(Performer, PerformerAdmin)
