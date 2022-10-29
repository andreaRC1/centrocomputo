from django.db import models


class Equipo(models.Model):
    tipo = models.CharField("Tipo", max_length=30, unique=False)
    marca = models.CharField("Marca", max_length=30, unique=False)
    modelo = models.CharField(
        "Modelo",
        max_length=30,
        unique=False,
        blank=True,
        null=True)

    DISPONIBLE_CHOICES = [
        ('D', 'Disponible'),
        ('ND', 'No disponible'),
    ]
    disponibilidad = models.CharField(
        "Disponibilidad",
        max_length=20,
        choices=DISPONIBLE_CHOICES,
    )
    descripcion = models.CharField(
        'Descripción',
        max_length=250,
        null=True,
        blank=True)

    def __str__(self):
        return self.tipo + " " + self.marca + " " + self.modelo
