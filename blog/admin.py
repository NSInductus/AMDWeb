from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("name", "order", "menu")
    ordering = ("order", "-updated")
    search_fields = ("name", "description")
    list_filter = ("menu",)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("title", "author", "public", "post_categories")
    ordering = ("-updated",)
    search_fields = ("title", "description", "content", "author__username", "categories__name")
    list_filter = ("public", "author__username", "categories__name")

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"

    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('core/css/custom_ckeditor.css',)
        }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)