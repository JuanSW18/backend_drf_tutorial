from rest_framework import serializers
from tutorial.backend.models import Alumno, Curso, AlumnoCurso

# Los serializers daran la estrutura a los objetos
# podemos definir que campos se pueden mostrar de cada objeto
# si queremos mostrar todos los objetos podemos usar all


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        # La siguiente declaracion se puede sustituir por ['__all__']
        # ya que se pretende mostrar todos los datos del objeto
        #
        # Se debe tener cuidado si uno de los objetos es AutoField
        # ya que al crear un objeto, usaremos el serializador para validar
        # por lo que debemos quitar/omitir el campo AutoField ya que no será
        # enviado en el request
        fields = ['nombres', 'apellidos', 'codigo']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['__all__']

class AlumnoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumnoCurso
        fields = ['__all__']
