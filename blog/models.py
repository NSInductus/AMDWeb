from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200, verbose_name="Título")
    description=models.CharField(max_length=200, verbose_name="Descripción")
    order=models.IntegerField(verbose_name="Ordenación")
    menu=models.BooleanField(verbose_name="¿Visible en menú?")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated=models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=200, verbose_name="Título")
    description=models.TextField(verbose_name="Descripción")
    content=RichTextField(verbose_name="Contenido", default="")
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts") 
    public=models.BooleanField(verbose_name="¿Visible?")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated=models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["-updated"]

    def __str__(self):
        return self.title