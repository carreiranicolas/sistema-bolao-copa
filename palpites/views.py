from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Sum
from campeonato.models import Jogo, Configuracao
from .models import Palpite
from .forms import PalpiteForm


# Create your views here.

def lista_jogos(request):

    agora = timezone.now()

    jogos_disponiveis = Jogo.objects.filter(
        data_hora__gt=agora,
        encerrado=False 
    ).order_by('data_hora')

    context = {
        'jogos': jogos_disponiveis
    }

    return render(request, 'palpites/lista_jogos.html', context=context)


@login_required
def palpitar(request, jogo_id):

    jogo = get_object_or_404(
        Jogo,
        pk=jogo_id
    )

    configuracao = Configuracao.objects.first()

    if (
        jogo.data_hora <= timezone.now()
        or not configuracao.palpites_abertos
    ):
        return render(
            request,
            'palpites/palpites_fechados.html',
            {'jogo': jogo}
        )


    palpite_existente = Palpite.objects.filter(
        usuario=request.user,
        jogo=jogo
    ).first()

    if request.method == 'POST':
        form = PalpiteForm(
            request.POST,
            instance=palpite_existente
        )

        if form.is_valid():
            palpite = form.save(commit=False)

            palpite.usuario = request.user

            palpite.jogo = jogo 

            palpite.save()

            return redirect('palpites:lista_jogos')
    
    else:
        form = PalpiteForm(
            instance=palpite_existente
        )

    context = {
        'jogo': jogo,
        'form': form
    }

    return render(request, 'palpites/palpitar.html', context=context)

@login_required
def meus_palpites(request):

    palpites = Palpite.objects.filter(
        usuario=request.user
    ).select_related(
        'jogo',
        'jogo__time_casa',
        'jogo__time_fora'
    ).order_by('jogo__data_hora')

    return render(request, 'palpites/meus_palpites.html', {'palpites': palpites})

@login_required
def ranking(request):

    ranking = (
        User.objects.
        annotate(
            total_pontos = Sum('palpite__pontuacao')
        )
        .order_by('-total_pontos')
    )

    return render(request, 'palpites/ranking.html', {'ranking': ranking})