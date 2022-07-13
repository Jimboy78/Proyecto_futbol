from django.db import models

# Create your models here.

#class Integrantes_Equipo(models.Model):
#    nombre = models.CharField(max_length=50)
#    apellido = models.CharField(max_length=50)
#    edad = models.IntegerField()
#    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)
#    posicion = models.CharField(max_length=50)
#    goles = models.IntegerField()
#
#    def __str__(self):
#        return self.nombre, self.apellido

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
    localidad = models.CharField(max_length=50)
    #jugador = models.ForeignKey(Integrantes_Equipo, on_delete=models.CASCADE, related_name='jugador')

    class Meta:
        ordering = ['posicion']

    def __str__(self):
        return self.nombre
