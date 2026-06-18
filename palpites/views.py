from django.shortcuts import render

# Create your views here.

def lista_jogos(request):
    return render(request, 'palpites/lista_jogos.html')


def palpitar(request):
    return render(request, 'palpites/palpitar.html')


def meus_palpites(request):
    return render(request, 'palpites/meus_palpites.html')

def ranking(request):
    return render(request, 'palpites/ranking.html')