from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    comision = models.IntegerField()

class Instructor(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)



class Alumnos(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()