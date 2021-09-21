from django.contrib import admin
from .models import FormContact

class FormContactAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)
    list_display = ("name", "email", "description", "created")
    ordering = ("-created",)
    search_fields = ("name", "email", "description", "content")

# Register your models here.
admin.site.register(FormContact, FormContactAdmin)
