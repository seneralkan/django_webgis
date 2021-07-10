from django.contrib import admin
from django.db import models
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
from .models import Incidences, counties

class IncidencesModelAdmin(LeafletGeoAdmin):
    list_display = ['name', 'localname']

class CountiesModelAdmin(LeafletGeoAdmin):
    list_display = ['adm1_en', 'adm0_en']

admin.site.register(Incidences,IncidencesModelAdmin)
admin.site.register(counties,CountiesModelAdmin)