from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    content = RichTextField(verbose_name="Contenido", default="")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects", null=True, blank=True)
    order = models.SmallIntegerField(verbose_name="Ordenación", default=0)
    public = models.BooleanField(verbose_name="¿Visible?")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['order','-updated']

    def __str__(self):
        return self.title