from django.urls import path
from .views import HomePageView, CVPageView

core_patterns = ([
    path('', HomePageView.as_view(), name="home"),
    path('cv/', CVPageView.as_view(), name="cv"),
], 'core')