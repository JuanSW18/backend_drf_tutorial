from django.contrib import admin
from django.urls import path, include
from tutorial.backend import views as v

urlpatterns = [
    path('list_alumnos', v.alumno_list),
    path('list_alumnos_v2', v.alumno_list),
    path('alumno_nuevo', v.alumno_nuevo),
    path('alumno', v.alumnos),
    path('alumno/<int:id>', v.get_alumno_by_id),
]

# Endpoints
# localhost:8000/list_alumnos
# ...
# POSTMAN: herramienta para probar consultas
#
# Extra:
# https://idratherbewriting.com/learnapidoc/docapis_doc_parameters.html-
