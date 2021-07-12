from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import counties, town, warehouse
from django.core.serializers import serialize
from django.http import HttpResponse
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def county_dataset(request):
    county  = serialize('geojson', counties.objects.all())
    return HttpResponse(county, content_type = 'json')

def town_dataset(request):
    l_town  = serialize('geojson', town.objects.all())
    return HttpResponse(l_town, content_type = 'json')

def warehouse_dataset(request):
    l_warehouse  = serialize('geojson', warehouse.objects.all())
    return HttpResponse(l_warehouse, content_type = 'json')