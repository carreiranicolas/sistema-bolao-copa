from django.core.management.base import BaseCommand

from palpites.models import Palpite


class Command(BaseCommand):

    help = 'Recalcula a pontuação de todos os palpites'

    def handle(self, *args, **options):

        palpites = Palpite.objects.all()

        total = palpites.count()

        self.stdout.write(
            f'Recalculando {total} palpites...'
        )

        for palpite in palpites:
            palpite.calcular_pontuacao()

        self.stdout.write(
            self.style.SUCCESS(
                'Pontuações recalculadas com sucesso!'
            )
        )