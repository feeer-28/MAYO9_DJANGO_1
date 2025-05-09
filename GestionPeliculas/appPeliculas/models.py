from django.db import models

# Create your models here.
class Genero(models.Model):
    genNombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.genNombre

class Pelicula(models.Model):
    pelCodigo = models.CharField(max_length=10, unique=True)
    pelTitulo = models.CharField(max_length=100)
    pelProtagonista = models.CharField(max_length=100)
    pelDuracion = models.IntegerField()
    pelResumen = models.TextField(max_length=500)
    pelFoto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    pelGenero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    def __str__(self):
        return self.pelTitulo