from django.db import models

CICLOS = (('I', 'I'),
          ('II', 'II'),
          ('III', 'III'),
          ('IV', 'IV'),
          ('V', 'V'),
          ('VI', 'VI'),
          ('VII', 'VII'),
          ('VIII', 'VIII'),
          ('IX', 'IX'),
          ('X', 'X'),)

# Create your models here.


class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=8)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)

    class Meta:
        db_table = 'ALUMNOS'


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    curso_nombre = models.CharField(max_length=25)
    creditos = models.IntegerField()
    ciclo = models.CharField(max_length=4, choices=CICLOS)

    class Meta:
        db_table = 'CURSOS'

class AlumnoCurso(models.Model):
    id_alumno_curso = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ALUMNOS_CURSOS'
