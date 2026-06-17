from django.db import models
from django.contrib.auth.models import User
from campeonato.models import Jogo

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
        f'{self.usuario.username} - {self.jogo}'
