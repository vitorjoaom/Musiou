from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def index(request):
    return render(request,'home.html')
    dados = {
        1: {
            "nome": "Chico",
            "música": "Complicated"
        },
        2:{
            "nome":"João",
            "música":"I'm with you"
        }
    }


def musik(requisicao):
    return render(requisicao, 'musik.html')

def home(requisicao):
    return render(requisicao, 'home.html')

def cadastrar(requisicao):
    return render(requisicao, 'cadastra.html')

def not_found(requisicao, exception):
    return render(requisicao, '404.html')