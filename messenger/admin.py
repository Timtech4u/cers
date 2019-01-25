from django.contrib import admin
from .models import *

admin.site.register(Hook)

class UnitAdmin(admin.ModelAdmin):
    list_filter = ('state', 'ward')
    list_display = ('location', 'lat', 'lon')

admin.site.register(Units, UnitAdmin)
