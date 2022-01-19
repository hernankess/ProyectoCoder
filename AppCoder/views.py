# from http.client import HTTPResponse
# from django.shortcuts import render

# # Create your views here.

# def inicio(request):
#     return HTTPResponse ("INICIO")

from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)


def inicio(request):
    return HttpResponse ("Inicio")
    #   return render(request, "AppCoder/inicio.html")

def cursos(request):
    return HttpResponse ("cursos")

    #   return render(request, "AppCoder/cursos.html")

def profesores(request):
    return HttpResponse ("profesores")

    #   return render(request, "AppCoder/profesores.html")


def estudiantes(request):
    return HttpResponse ("estudiantes")

    #   return render(request, "AppCoder/estudiantes.html")


def entregables(request):
    return HttpResponse ("entregable")

    #   return render(request, "AppCoder/entregables.html")