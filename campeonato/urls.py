from django.urls import path
from . import views

app_name = 'campeonato'

urlpatterns = [
    path('', views.home, name='home'),
    path('jogos/', views.jogos, name='jogos'),
    path('regras/', views.regras, name='regras')
]