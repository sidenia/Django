from django.shortcuts import render, get_list_or_404, get_object_or_404
#from django.http import HttpResponse
from .models import *

def homepage(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    context = {
        'receitas': receitas
    }
    return render(request,'index.html', context)





def receita(request, receita_id):
    #armazenar o objeto que vem do filtro da url e pega o models e diz que o valor que vem na url é o id da receita
    receita = get_object_or_404(Receita, pk=receita_id)

    #devolve no dicionário contexto a receita correspondente a esse ID.
    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_a_exibir)




def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar'] #nome que tiver no request
        if nome_a_buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas' : lista_receitas
    }
    return render(request, 'buscar.html', dados)