from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
# Create your views here.

def index(request):
    dados = {
    1: {'nome': 'João Grilo',
        'telefone': '(83) 992343211'},
    2: {'nome': 'Chicó',
        'telefone': '(83) 992343212'},
    3: {'nome': 'Rosinha',
        'telefone': '(83) 992343213'},
    4: {'nome': 'Padeiro',
        'telefone': '(83) 992343214'},
    5: {'nome': 'Dora',
        'telefone': '(83) 992343215'}
}
    return render(request, 'contatos/index.html',  {"conts": dados})

def contato(request):
    return render(request, 'contatos/det_contato.html')
