from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("title", "order", "public")
    ordering = ("order", "-updated")
    search_fields = ("title", "description", "content", "image")
    list_filter = ("public",)

    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('core/css/custom_ckeditor.css',)
        }

# Register your models here.
admin.site.register(Project, ProjectAdmin)