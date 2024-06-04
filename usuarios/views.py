from django.shortcuts import render
from usuarios.forms import loginForms

# Create your views here.
def login(request):
    forms = loginForms()
    return render(request, 'usuarios/login.html', {'form':forms})

def logout(request):
    return render(request, 'usuarios/logout.html')

def cadastrar(request):
    return render(request, 'usuarios/cadastrar.html')

