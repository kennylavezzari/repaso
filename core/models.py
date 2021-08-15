from django.db import models

class auto(models.Model):
    marca=models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="imagenes")
    contentenido = models.TextField()
    fecharegistro=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.marca

class chofer(models.Model):
    nombre=models.CharField(max_length=100)
    foto = models.ImageField(upload_to="imagenes")
    contentenido = models.TextField()
    fecharegistro=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
# Create your models here.
