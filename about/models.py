from django.db import models

# Create your models here.
class Course(models.Model):
    institution = models.CharField(max_length=200, verbose_name="Institución")
    description = models.CharField(max_length=800 ,verbose_name="Descripción del curso")
    extra = models.CharField(max_length=800 ,verbose_name="Información extra", null=True, blank=True)
    start_date = models.DateTimeField(verbose_name="Fecha de inicio del curso")
    finish_date = models.DateTimeField(verbose_name="Fecha de finalización del curso", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="about", null=True, blank=True)
    order = models.SmallIntegerField(verbose_name="Ordenación", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['order','-updated']

    def __str__(self):
        return self.institution + " - " + self.description

# Create your models here.
class Job(models.Model):
    institution = models.CharField(max_length=200, verbose_name="Institución")
    description = models.CharField(max_length=800 ,verbose_name="Descripción del trabajo")
    extra = models.CharField(max_length=800 ,verbose_name="Información extra", null=True, blank=True)
    start_date = models.DateTimeField(verbose_name="Fecha de inicio del trabajo")
    finish_date = models.DateTimeField(verbose_name="Fecha de finalización del trabajo", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="about", null=True, blank=True)
    order = models.SmallIntegerField(verbose_name="Ordenación", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'
        ordering = ['order','-updated']

    def __str__(self):
        return self.institution + " - " + self.description
        