from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import FormContact
from django.urls import reverse_lazy

class FormContactCreate(CreateView):
    model = FormContact
    fields = ['name', 'email', 'description', 'content']
    template_name = "contact/contact_form.html"
    def get_success_url(self):
        return reverse_lazy("contact:send-message")+"?ok"