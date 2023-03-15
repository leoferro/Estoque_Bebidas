from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    # precisamos combinar entre templates e views sobre quais parametros as views vão passar
    parametro = "---Parametro Passado pela view---"

    #Carrego o template
    template = loader.get_template("criar_paginas.html")

    #Renderiza o template e passa o parametro
    return HttpResponse(template.render({"nome_do_parametro":parametro}, request))

def qtd(request, quantidade):
    dobro = quantidade*2
    template = loader.get_template("passar_param.html")
    return HttpResponse(template.render({"dobro": dobro}, request))