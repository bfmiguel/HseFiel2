from django.shortcuts import render, redirect
from AppHse.models import analisis_De_Riesgo
from django.http import HttpResponse
from AppHse.forms import permisotrabajoForms

def hsecampo(request):
    analisis = analisis_De_Riesgo.objects.all()
    contexto = {
        "analisis" : analisis_De_Riesgo
    }

    return render(request, "AppHse/HseCampo.html", contexto)

def documentos(request):
    analisis = analisis_De_Riesgo(nombre="DTM", Operacion="Drilling")
    analisis.save()
    contexto = {"analisis" : analisis}

    return HttpResponse(f" Se verifico el documento {analisis.nombre} durante las operaciones de {analisis.Operacion}")

def permiso_trabajo_from(request):

    if request.method == "POST":
        return redirect("app/permiso_trabajo/")

    permiso_trabajo_formulario = permisotrabajoForms()
    contexto = {
        "form": permiso_trabajo_formulario

    }

    return render(request, "AppHse/permisotrabajo.html", contexto)

def show_html(request):
    contexto = {'nombre': 'Sup. Miguel Batista'}
    return render(request, 'index.html', contexto)