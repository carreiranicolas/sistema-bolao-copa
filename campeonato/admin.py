from django.contrib import admin
from palpites.models import Palpite
from .models import Time, Jogo, DiaJogo, Configuracao

# Register your models here.


@admin.register(Configuracao)
class ConfiguracaoAdmin(admin.ModelAdmin):

    list_display = (
        'pontos_placar_exato',
        'pontos_resultado',
        'palpites_abertos',
        'criterio_desempate_1',
        'criterio_desempate_2'
    )

    def has_add_permission(self, request):
        return not Configuracao.objects.exists() #permite adicionar somente se o objeto não existir



admin.site.register(Time)

admin.site.register(DiaJogo)

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):

    #Abaixo temos um método que ao salvar o resultado do jogo, pega todos os palpites
    # relacionados a esse jogo e calcula a pontuação

    def save_model(
        self,
        request,
        obj,
        form,
        change
    ):
        super().save_model(
            request,
            obj,
            form,
            change
        )

        if (
            obj.gols_casa is not None
            and
            obj.gols_fora is not None
        ):
            palpites = Palpite.objects.filter(
                jogo=obj
            )

            for palpite in palpites:
                palpite.calcular_pontuacao()