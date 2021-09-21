from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "core/home.html"

class CVPageView(TemplateView):
    template_name = "core/cv.html"