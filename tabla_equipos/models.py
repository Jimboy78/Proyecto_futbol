from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    puntos = models.IntegerField()
    partidos_ganados = models.IntegerField()
    partidos_perdidos = models.IntegerField()
    partidos_empatados = models.IntegerField()
    goles_favor = models.IntegerField()
    goles_contra = models.IntegerField()
    diferencia_goles = models.IntegerField()
    posicion = models.IntegerField()

    class Meta:
        ordering = ['posicion']

    def __str__(self):
        return self.nombre
