from django.shortcuts import render
from .models import Configuracao

# Create your views here.


def home(request):
    return render(request, 'campeonato/home.html')


def jogos(request):
    return render(request, 'campeonato/jogos.html')

def regras(request):

    configuracao = Configuracao.objects.first()

    context = {
        'configuracao': configuracao
    }


    return render(request, 'campeonato/regras.html', context=context)