from django.urls import path
from .views import AboutListView

about_patterns = ([
    path('', AboutListView.as_view(), name="about"),
], 'about')