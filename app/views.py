# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from buscador import settings
import requests  
import json
# Create your import requestsviews here.
#           IMPORTANTE!!!!!
# sudo pip install requests
def Buscador(request):
    if request.method == 'POST':
        Datos = request.POST
        print (Datos)
        #url = "http://localhost:8888/buscar"
        #data = {"oracion":"as","idPersona":"000000","tipoAcceso":1,"coordX":"1234","coordY":"1234"}
        #headers = {'content-type': 'application/json'}
        #r=requests.post(url, data=json.dumps(data), headers=headers)
        #r.text
        #received_json_data=json.loads(request.body)
        #print(received_json_data)
        oracion = Datos["textobusqueda"]
        r = requests.get('http://localhost:8011/busqueda/' + oracion + '/')
        json = r.json()
        oResultados = []
        Negocios = json["resultado"]
        for Negocio in Negocios:
            oNegocio = {}
            oNegocio["nombre"] = Negocio["nombre"]
            oNegocio["imagen"] = Negocio["imagen"]
            oNegocio["descripcion"] = Negocio["descripcion"]
            oNegocio["id"] = Negocio["id"]
            oNegocio["categoriaTexto"] = Negocio["categoriaTexto"]
            #oNegocio["raitingEntero"] = int(Negocio["raiting"])
            oNegocio["raitingEntero"] = range(1, int(Negocio["raiting"])+1)

            oNegocio["raitingPacial"] = Negocio["raiting"]-int(Negocio["raiting"])
            #oNegocio["raitingFaltante"] = 5-int(Negocio["raiting"])
            oNegocio["raitingFaltante"] = range(1, int(5-int(Negocio["raiting"]))+1)
            oResultados.append(oNegocio)
        #print Negocios
        return render(request, 'resultadoBusqueda.html',  {"oResultados": oResultados,"oracion":oracion})
    else:
        return render(request, 'index.html', {})

def Contacto(request):
    return render(request, 'contacto.html', {})

def Acercade(request):
    return render(request, 'acercade.html', {})

def Dirayacucho(request):
    return render(request, 'dirayacucho.html', {})