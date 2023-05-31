from django.db import models

# Create your models here.

class Especialidad(models.Model):
    idEspecialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre

class Docente(models.Model):
    idDocente = models.AutoField(primary_key=True)
    apellido = models.CharField(max_length = 50)
    nombre = models.CharField(max_length = 50)
    fIngreso = models.DateField()
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    codigo = models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveIntegerField()
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Matricula(models.Model):
    idMatricula = models.AutoField(primary_key=True)
    idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fechaMat = models.DateField()
    cuotas =  models.PositiveIntegerField()
