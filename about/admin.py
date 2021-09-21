from django.contrib import admin
from .models import Course, Job

class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("institution", "description", "start_date", "finish_date")
    ordering = ("order", "-start_date")
    search_fields = ("institution", "description", "extra")

class JobAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("institution", "description", "start_date", "finish_date")
    ordering = ("order", "-start_date")
    search_fields = ("institution", "description", "extra")

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Job, JobAdmin)