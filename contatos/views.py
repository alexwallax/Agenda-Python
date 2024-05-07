from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
# Create your views here.

def index(request):
    return render(request, 'contatos/index.html')

def contato(request):
    return render(request, 'contatos/det_contato.html')
