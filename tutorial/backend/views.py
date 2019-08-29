from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from tutorial.backend import models as m
from tutorial.backend import serializers as s

# Create your views here.

# Funcion con return JsonResponse
def alumno_list(request):
    alumno = m.Alumno.objects.all()
    # El atributo many nos indica que recibiremos muchos objetos
    # si omitimos este atributo nos puede arrojar una excepcion
    serializer = s.AlumnoSerializer(alumno, many=True)
    return JsonResponse(serializer.data, safe=False)


# Funcion con return Response
def alumno_list_v2(request):
    alumno = m.Alumno.objects.all()
    serializer = s.AlumnoSerializer(alumno, many=True)
    return Response(serializer.data, content_type='application/json')


# El decorador @api_view nos ayuda a delimitar
# los metodos aceptados por la funcion
@api_view(['POST'])
def alumno_nuevo(request):
    serializer = s.AlumnoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, content_type='application/json')


# Ejemplo con varios metodos de acceso
@api_view(['GET', 'POST'])
def alumnos(request):
    if request.method == 'GET':
        alumno = m.Alumno.objects.all()
        serializer = s.AlumnoSerializer(alumno, many=True)
        return Response(serializer.data, content_type='application/json')
    else:
        serializer = s.AlumnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, content_type='application/json')


# Funcion con un parametro y manejo de excepciones
@api_view(['GET'])
def get_alumno_by_id(request, id):
    try:
        # El metodo get se usa cuando estamos seguros que solo recibiremos 1 objeto
        # si se recibe más de 1 objeto se generará un error
        alumno = m.Alumno.objects.get(id_alumno=id)
        serializer = s.AlumnoSerializer(alumno)
        return Response(serializer.data, content_type='application/json')
    except m.Alumno.DoesNotExist:
        return Response('ID_ALUMNO NO EXISTE!', content_type='application/json')
