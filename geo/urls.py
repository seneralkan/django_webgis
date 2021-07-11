from django.urls.conf import path
from .views import HomePageView, county_dataset
from django.conf.urls import include, url

urlpatterns = [
    path('', HomePageView.as_view(), name = 'homepage'),
    path('county-data/', county_dataset, name = 'county'),
    path('incident-data/', HomePageView.as_view(), name = 'incident'),
]
