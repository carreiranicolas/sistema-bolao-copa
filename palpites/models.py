from django.db import models
from django.contrib.auth.models import User
from campeonato.models import Jogo, Configuracao

# Create your models here.



class Palpite(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)

    gols_casa = models.PositiveSmallIntegerField()
    gols_fora = models.PositiveSmallIntegerField()

    pontuacao = models.PositiveSmallIntegerField(default=0)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('usuario', 'jogo')
        verbose_name = 'Palpite'
        verbose_name_plural = 'Palpites'

    def __str__(self):
        return f'{self.usuario.username} - {self.jogo}'
    

    def resultado(self):
        if self.gols_casa > self.gols_fora:
            return 'casa'
        
        if self.gols_fora > self.gols_casa:
            return 'fora'
        
        return 'empate'

    
    def calcular_pontuacao(self):
        jogo = self.jogo
        configuracao = Configuracao.objects.first()

        if (
            jogo.gols_casa is None 
            or jogo.gols_fora is None
        ):
            self.pontuacao = 0
            self.save()
            return

        

        #Placar exato

        if(
            self.gols_casa == jogo.gols_casa
            and
            self.gols_fora == jogo.gols_fora
        ):
            self.pontuacao = configuracao.pontos_placar_exato

        #Resultado correto (não acertou o placar, mas sim, quem ganhou/perdeu)

        elif self.resultado() == jogo.resultado():
            self.pontuacao = configuracao.pontos_resultado
        
        else:
            self.pontuacao = 0
        
        self.save()

