from django.db import models


# Create your models here.

class Curso(models.Model):
    nombre= models.CharField(max_length=50)
    comision= models.IntegerField()
    #creamos un curso que va a tener un nombre y una comision (modelo creado guardado en base de datos)

class Estudiante(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)

class Entregable(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_entrega= models.DateField()
    entregado= models.BooleanField()


# hereda de model un MODELO (tipo de base de dato, sale de models)

