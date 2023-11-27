from django.shortcuts import render
from AppHse.models import analisis_De_Riesgo
from django.http import HttpResponse


def documentos(request):
    analisis = analisis_De_Riesgo(nombre="DTM", Operacion="Drilling")
    analisis.save()
    contexto = {"analisis" : analisis}

    return HttpResponse(f" Se verifico el documento {analisis.nombre} durante las operaciones de {analisis.Operacion}")


def show_html(request):
    contexto = {'nombre': 'Sup. Miguel Batista'}
    return render(request, 'index.html', contexto)