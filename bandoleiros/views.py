from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Personagens

def main(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def personagens(request):
    ctxt = {
        'colunas': ("Nome","Apelido","Ano de nascimento","Signo"),
        'personagens': Personagens.objects.all().values()
    }
    
    template = loader.get_template("personagens.html")
    return HttpResponse(template.render(ctxt,request))

def info(request):
    ctxt = {
        'p': Personagens.objects.all()[0]
    }
    
    template = loader.get_template("info.html")
    return HttpResponse(template.render(ctxt,request))