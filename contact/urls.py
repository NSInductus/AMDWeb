from django.urls import path
from .views import FormContactCreate

contact_patterns = ([
    path('', FormContactCreate.as_view(), name="send-message"),
], 'contact')