from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Time(models.Model):
    nome = models.CharField(max_length=45, unique=True)
    sigla = models.CharField(max_length=3, unique=True)
    bandeira = models.ImageField(upload_to='bandeiras/')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'



class DiaJogo(models.Model):
    data = models.DateField(unique=True)

    class Meta:
        verbose_name = 'Dia Jogo'
        verbose_name_plural = 'Dia Jogos'

    def __str__(self):
        return str(self.data)



class Jogo(models.Model):
    dia_jogo = models.ForeignKey(DiaJogo, on_delete=models.CASCADE)
    time_casa = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='jogos_como_casa')
    time_fora = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='jogos_como_fora')
    data_hora = models.DateTimeField()
    gols_casa = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )
    gols_fora = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )
    encerrado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.time_casa} x {self.time_fora}"
    
    class Meta:
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"

    def clean(self):
        if self.time_casa == self.time_fora:
            raise ValidationError(
                'Um mesmo time não pode jogar contra ele mesmo'
            )


class Configuracao(models.Model):
    pontos_placar_exato = models.PositiveIntegerField(default=5)
    pontos_resultado = models.PositiveIntegerField(default=3)
    palpites_abertos = models.BooleanField(default=True)
    
    CRITERIOS = [

        ('placares_exatos', 'Maior número de placares exatos'),
        ('acertos_resultado', 'Maior número de resultados corretos'),
        ('data_cadastro', 'Cadastro mais antigo'),
    ]
    
    criterio_desempate_1 = models.CharField(
        max_length=30,
        choices=CRITERIOS
    )
    
    criterio_desempate_2 = models.CharField(
        max_length=30,
        choices=CRITERIOS
    )

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'

    def __str__(self):
        return 'Configuração do sistema'
    
    def clean(self):
        if self.criterio_desempate_1 == self.criterio_desempate_2:
            raise ValidationError(
                'Os critérios de desempate 1 e 2 não podem ser iguais'
            )