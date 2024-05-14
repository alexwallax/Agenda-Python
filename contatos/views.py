from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from contatos.models import Contato
# Create your views here.

def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html',  {'cont': contatos})

def contato(request):
    return render(request, 'contatos/det_contato.html')
