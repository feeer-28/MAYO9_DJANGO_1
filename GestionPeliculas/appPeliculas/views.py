from django.shortcuts import render
from django.db import Error
from appPeliculas.models import Pelicula, Genero
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

@csrf_exempt
def agregarGenero(request):
    try: 
        nombre = request.POST['txtNombre']
        genero = Genero(genNombre=nombre)
        genero.save()
        mensaje = "Genero guardado correctamente"
    except Error as e:
        mensaje = str(e)
    retorno = {"mensaje": mensaje}
    return JsonResponse(retorno)
