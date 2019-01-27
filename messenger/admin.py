from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# TODO: Fix
@admin.register(Report)
class ReportsResource(ImportExportModelAdmin):

    def get_sortable_by(self, request):
        return ''

class UnitAdmin(admin.ModelAdmin):
    list_filter = ('state', 'ward')
    list_display = ('location', 'lat', 'lon')

admin.site.register(Hook)
admin.site.register(Units, UnitAdmin)
