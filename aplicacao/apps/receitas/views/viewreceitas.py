from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import *
#paginação
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def homepage(request):
    """ pagina inicial para usuario nao logado """
    #query receitas = Receota.objects.all() assim traria todas as receitas, independente da flag publicada
    
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    
    # paginação
    paginator = Paginator(receitas, 6)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    context = {
        'receitas': receitas_por_pagina,
    }
    return render(request,'receitas/index.html', context)


def receita(request, receita_id):
    """ Exibe as receitas na pagina inicial """
    #armazenar o objeto que vem do filtro da url e pega o models e diz que o valor que vem na url é o id da receita
    receita = get_object_or_404(Receita, pk=receita_id)

    #devolve no dicionário contexto a receita correspondente a esse ID.
    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receitas/receita.html', receita_a_exibir)


###################  incluir validacoes
def criareceita(request):
    """ Criacao de novas receitas """
    # os campos dentro dicionario POST no if são == ao "name" do html cria receita
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']

        # A requisição traz o id do usuario e atraves desse metodo get_object_or_404
        # podemos pegar esse dado e passar na variável user
        # primeira propriedade do metodo é a Classe que se quer pegar
        # a segunda é qual o id do objeto que se quer gerar
        user = get_object_or_404(User, pk=request.user.id)

        # criar um objeto receita: para fazer o models enviar esses dados para o BD.
        receita = Receita.objects.create(pessoa=user, 
                                        nome_receita=nome_receita, 
                                        ingredientes=ingredientes, 
                                        modo_preparo=modo_preparo, 
                                        tempo_preparo=tempo_preparo, 
                                        rendimento=rendimento, 
                                        categoria=categoria, 
                                        foto_receita=foto_receita)
        #salva no BD
        receita.save()
        
        return redirect('usuarios/dashboard')

    else:
        return render(request, 'receitas/criareceita.html')


    # if request.user.is_authenticated:
    #     return render(request, 'usuarios/criareceita.html')
    # else:
    #     return redirect('home')


def deletareceita(request, receita_id):
    """ Deleção de receitas """
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()    
    return redirect('dashboard')


def editareceita(request, receita_id):
    """ Redireciona para pagina de Edicao de receitas """
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {'receita': receita }
    return render(request,'receitas/editareceita.html', receita_a_editar)


def atualizareceita(request):
    """ Atualização de receitas """
    if request.method == 'POST':
        #tras a info do id hidden que ta no template edita receita
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        
        r.save()
        return redirect('dashboard')
