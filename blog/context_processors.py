from blog.models import Category, Post

def get_categories(request):
    #Id de categorias usadas en articulos publicados para futura subconsulta
    ids_categories_in_use=Post.objects.filter(public=True).values_list("categories", flat=True)
    categories=Category.objects.filter(id__in=ids_categories_in_use).filter(menu=True).order_by("order").values_list("id", "name")
    return {
        "categories":categories
    }