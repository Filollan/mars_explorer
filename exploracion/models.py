from django.db import models

class Mision(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Astronauta(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50)
    mision = models.ForeignKey(Mision, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Experimento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    mision = models.ForeignKey(Mision, on_delete=models.CASCADE)
    resultado = models.TextField()

    def __str__(self):
        return self.titulo
