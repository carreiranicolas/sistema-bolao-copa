from django.urls import path
from . import views

app_name = 'palpites'

urlpatterns = [
    path('', views.lista_jogos, name='lista_jogos'),
    path('jogo/<int:jogo_id>/', views.palpitar, name='palpitar'),
    path('meus-palpites', views.meus_palpites, name='meus_palpites'),
    path('ranking/', views.ranking, name='ranking')
]
