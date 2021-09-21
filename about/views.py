from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from .models import Course, Job


# Create your views here.
class AboutListView(ListView):
    model = Course
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutListView, self).get_context_data(**kwargs)
        context.update({
            'job_list': Job.objects.all(),
        })
        return context