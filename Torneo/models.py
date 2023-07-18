from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Torneo(models.Model):
    numero_equipos = models.IntegerField()
    nombre = models.CharField(max_length=20)


class Fecha(models.Model):
    torneo_id = models.ForeignKey(Torneo, on_delete=models.CASCADE)


class Partido(models.Model):
    fecha_id = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    fecha_partido = models.DateTimeField(datetime.now)
    goles_local = models.PositiveIntegerField()
    goles_visitante = models.PositiveIntegerField()
    puntos_local = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    puntos_visitante = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])


class Equipo(models.Model):
    nombre = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=20)
    encargado = models.CharField(max_length=20)
    celular = models.IntegerField(validators=[MaxValueValidator(9999999999)])


class Partido_Equipo(models.Model):
    partido_id = models.ForeignKey(Partido, on_delete=models.CASCADE)
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_equipo_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_equipo_visitante')


class Judador(models.Model):
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    identificacion = models.CharField(max_length=25)
    nacimiento = models.DateField(null=False)


class Tecnico(models.Model):
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    identificacion = models.CharField(max_length=25)
