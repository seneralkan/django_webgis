from django.urls.conf import path
from .views import HomePageView
from django.conf.urls import include, url

urlpatterns = [
    path('', HomePageView.as_view(), name = 'homepage'),
]
