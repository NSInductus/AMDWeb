from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Project


# Create your views here.
class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    queryset = Project.objects.filter(public = True)
    paginate_by = 3
    

class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/project_detail.html"