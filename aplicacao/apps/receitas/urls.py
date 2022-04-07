from django.urls import path

from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('<int:receita_id>', receita, name='receita'),
    path('buscar', busca, name='buscar'),
    path('criareceita', criareceita, name='criareceita'),
    path('deleta/<int:receita_id>', deletareceita, name='deletareceita'),
    path('edita/<int:receita_id>', editareceita, name='editareceita'),
    path('atualiza', atualizareceita, name='atualizareceita'),
]