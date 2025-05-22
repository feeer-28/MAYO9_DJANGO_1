from django.shortcuts import render
from django.db import Error
from appPeliculas.models import Pelicula, Genero
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def vistaAgregarGenero(request):
    return render(request, 'agregarGenero.html')
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
    return render(request, 'agregarGenero.html', retorno)

def listarPeliculas(request):
    peliculas = Pelicula.objects.all().values()
    print(peliculas)
    retorno = {"peliculas": list(peliculas)}
    return JsonResponse(retorno, content_type='application/json')

def vistaListarPeliculas(request):
    peliculas = Pelicula.objects.all()
    print(peliculas)  # para revisar en la consola
    retorno = {"peliculas": peliculas}
    return render(request, "listarPeliculas.html", retorno)


def agregarPelicula(request):
    try:
        codigo = request.POST['txtCodigo']
        titulo = request.POST['txtTitulo']
        protagonista = request.POST['txtProtagonista']
        duracion = int(request.POST['txtDuracion'])
        resumen = request.POST['txtResumen']
        foto = request.FILES['fileFoto']
        idGenero = int(request.POST['cbGenero'])
        genero = Genero.objects.get(pk=idGenero)

        # crear objeto pelicula
        pelicula = Pelicula(pelCodigo=codigo,
                            pelTitulo=titulo,
                            pelProtagonista=protagonista,
                            pelDuracion=duracion,
                            pelResumen=resumen,
                            pelFoto=foto,
                            pelGenero=genero)

        pelicula.save()
        mensaje = "Pelicula agregada correctamente"
    except Exception as error:
        mensaje = str(error)
    
    retorno = {"mensaje": mensaje, "idPelicula": pelicula.id}
    return JsonResponse(retorno)

def vistaAgregarPelicula(request):
    generos = Genero.objects.all()
    retorno = {"generos": generos}
    return render(request, "agregarPelicula.html", retorno)

def consultarPeliculaPorId(request, id):
    pelicula = Pelicula.objects.get(pk=id)
    generos = Genero.objects.all()
    #retornamos los generos porque se necesitan en la interfaz
    retorno = {"pelicula": pelicula, "generos": generos}
    return render(request, "actualizarPelicula.html", retorno)

def actualizarPelicula(request):
    try:
        idPelicula = request.POST['idPelicula']
        peliculaActualizar = Pelicula.objects.get(pk=idPelicula)
        # Actualizar los campos de la película  
        peliculaActualizar.pelCodigo = request.POST['txtCodigo']
        peliculaActualizar.pelTitulo = request.POST['txtTitulo']
        peliculaActualizar.pelProtagonista = request.POST['txtProtagonista']
        peliculaActualizar.pelDuracion = int(request.POST['txtDuracion'])
        peliculaActualizar.pelResumen = request.POST['txtResumen']
        idGenero = int(request.POST['cbGenero'])
        genero = Genero.objects.get(pk=idGenero)
        peliculaActualizar.pelGenero = genero
        foto = request.FILES.get('fileFoto')

        if (foto):
            os.remove(os.path.join(settings.MEDIA_ROOT + "/" +
                                str(peliculaActualizar.pelFoto)))
            peliculaActualizar.pelFoto = foto
        peliculaActualizar.save()
        mensaje = "Pelicula actualizada correctamente"

    except Exception as error:
        mensaje = str(error)
    
    retorno = {"mensaje": mensaje}
    return JsonResponse(retorno)

def eliminarPelicula(request, id):
    try:
        peliculaEliminar = Pelicula.objects.get(pk=id)
        peliculaEliminar.delete()
        mensaje = "Pelicula eliminada correctamente"
    except Exception as error:
        mensaje = str(error)
    
    retorno = {"mensaje": mensaje}
    return JsonResponse(retorno)