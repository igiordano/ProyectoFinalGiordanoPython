from django.shortcuts import render

from MiApp.models import Curso

from MiApp.models import Instructor
from .forms import CrearCursoForm, CrearinstructorForm
# Create your views here.

def mostrar_curso(request):

    c1 = Curso(nombre='Programador', camada='2022')
    c2 = Curso(nombre='Programador Web', camada='2022')

    return render(request, 'MiApp/curso.html', {'curso':[c1, c2]})

def mostrar_instructor(request):
    i1= Instructor(nombre='Ignacio', apellido='Giordano', nacimiento='1991-03-15', email='ignaciogiordano03@gmail.com', profesion='Programador')
    i2= Instructor(nombre='Monica', apellido='Cora', nacimiento='1961-02-15', email='niquitacora53@gmail.com', profesion='Docente')

    return render(request, 'MiApp/instructor.html', {'instructor':[i1, i2]})

def mostrar_index(request):

    return render(request, 'MiApp/index.html')

def mostrar_referencias(request):

    return render(request, 'MiApp/referencias.html')

def crear_curso(request):

    if request.method == 'POST':

        formulario = CrearCursoForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            curso = Curso(nombre=formulario_limpio['nombre'], camada=formulario_limpio['camada'])

            curso.save()

            return render(request, 'MiApp/index.html')
    else:
        formulario = CrearCursoForm()

    return render(request, 'MiApp/crear_curso.html', {'formulario': formulario})


def crear_instructor(request):
    if request.method == 'POST':

        formulario = CrearinstructorForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            instructor = Instructor(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], email=formulario_limpio['email'], profesion=formulario_limpio['profesion']) 

            instructor.save()

            return render(request, 'MiApp/index.html')
    else: 

        formulario = CrearinstructorForm()
        return render(request, 'MiApp/crear_instructor.html', {'formulario': formulario})

def buscar_comision(request):

    if request.GET.get('comision', False): # -> 12345
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)

        return render(request, 'MiApp/buscar_comision.html', {'cursos': cursos})
    else:
        respuesta = 'No hay datos'
    return render(request, 'MiApp/buscar_comision.html', {'respuesta': respuesta})

def buscar_instructor(request):

    if request.GET.get('email', False):
        email = request.GET['email']
        instructores = Instructor.objects.filter(email__icontains=email)

        return render(request, 'MiApp/buscar_instructor.html', {'instructores': instructores})
    else:
        respuesta = 'No hay datos'
    return render(request, 'MiApp/buscar_instructor.html', {'respuesta': respuesta})