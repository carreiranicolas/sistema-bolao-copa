from django.shortcuts import render
from django.utils import timezone
from .models import Configuracao, Jogo

# Create your views here.


def home(request):

    agora = timezone.now()

    # Filtra os jogos onde data_hora é MAIOR que agora (gt = greater than)
    proximos_jogos = Jogo.objects.filter(data_hora__gt=agora).order_by('data_hora')[:5]

    
    context = {
        'jogos': proximos_jogos
    }

    return render(request, 'campeonato/home.html', context=context)


def jogos(request):

    todos_os_jogos = Jogo.objects.all()


    context = {
        'jogos': todos_os_jogos
    }

    return render(request, 'campeonato/jogos.html', context=context)

def regras(request):

    configuracao = Configuracao.objects.first()

    context = {
        'configuracao': configuracao
    }


    return render(request, 'campeonato/regras.html', context=context)