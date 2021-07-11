from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import counties
from django.core.serializers import serialize
from django.http import HttpResponse
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/index.html'

def county_dataset(request):
    county  = serialize('geojson', counties.objects.all())
    return HttpResponse(county, content_type = 'json')