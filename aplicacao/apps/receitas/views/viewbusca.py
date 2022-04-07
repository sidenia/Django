from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from receitas.models import *


def busca(request):
    """ pesquisa receita por nome """
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar'] #nome que tiver no request
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas' : lista_receitas
    }
    return render(request, 'receitas/buscar.html', dados)
