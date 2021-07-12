from django.contrib import admin
from django.db import models
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
from .models import Incidences, counties, town, warehouse

class IncidencesModelAdmin(LeafletGeoAdmin):
    list_display = ['name', 'localname']

class CountiesModelAdmin(LeafletGeoAdmin):
    list_display = ['adm1_en', 'adm0_en']

class TownModelAdmin(LeafletGeoAdmin):
    list_display = ['adm2_en', 'adm1_en']

class WarehouseModelAdmin(LeafletGeoAdmin):
    list_display = ['objectid', 'adm2_en']

admin.site.register(Incidences,IncidencesModelAdmin)
admin.site.register(counties,CountiesModelAdmin)
admin.site.register(town,TownModelAdmin)
admin.site.register(warehouse,WarehouseModelAdmin)