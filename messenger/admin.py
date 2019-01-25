from django.contrib import admin
from .models import *

admin.site.register(Hook)

class UnitAdmin(admin.ModelAdmin):
    list_filer = ('state', 'ward') #Fix this

admin.site.register(Units, UnitAdmin)
