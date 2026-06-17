from django.contrib import admin
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

admin.site.register(Jogo)