from django.urls import path
from MiApp.views import mostrar_curso, mostrar_index, mostrar_referencias, mostrar_instructor, mostrar_instructor, crear_curso, crear_instructor, buscar_comision, buscar_instructor

urlpatterns = [
    path('mostrar_curso/', mostrar_curso, name='Mostrar'),
    path('', mostrar_index),
    path('mostrar_referencias/', mostrar_referencias, name='Referencias'),
    path('crear_curso/', crear_curso, name='Crear Curso'),
    path('crear_instructor/', crear_instructor, name='Crear Instructor'),
    path('buscar_comision/', buscar_comision, name='Buscar Comision'),
    path('buscar_instructor/', buscar_instructor, name='Buscar Instructor')

]