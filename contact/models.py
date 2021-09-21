from django.db import models

# Create your models here.
class FormContact(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    email = models.EmailField(max_length=200, verbose_name="Correo Electronico")
    description = models.CharField(max_length=200, verbose_name="Asunto")
    content = models.TextField(max_length=1000, verbose_name="Contenido")
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de creación")

    class Meta():
        verbose_name = "Formulario de Contacto"
        verbose_name_plural = "Formularios de Contacto"
        ordering = ["-created"]
    
    def __str__(self):
        return self.description
    