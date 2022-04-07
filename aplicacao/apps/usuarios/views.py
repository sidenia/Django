from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita


def cadastro(request):
    """ Cadastra novo usuario no sistema """
    if request.method == 'POST': 
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.warning(request, 'O campo nome não pode ser vazio')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.warning(request, 'O campo email não pode ser vazio')
            return redirect('cadastro')

        if not senha.strip() and not senha2.strip():
            messages.warning(request, 'O campo senha não pode ser vazio')
            return redirect('cadastro')
        
        if senhas_nao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais!')
            return redirect('cadastro')
            
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'E-mail já cadastrado')
            return redirect('login')

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('login')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        messages.success(request, 'Cadastro concluído com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    """ Realiza o login de um usuario no sistema"""
    if request.method == 'POST':
        email = request.POST['email'] #esse é o name que vem do html na linha do input
        senha = request.POST['senha']
        
        if email == '' or senha == '':
            print('Senha e email não podem ficar em branco')  
            return redirect('login')
    
        print(email, senha)
        if User.objects.filter(email=email).exists():
            #pega o nome do usuario do email que veio no request no BD, se existir
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                print('login realizado com sucesso')
                return redirect('dashboard')
    
    return render(request, 'usuarios/login.html')


def logout(request): 
    """ Realiza o logout de um usuario no sistema"""
    auth.logout(request) 
    return (redirect('home'))


def dashboard(request):
    """ Apresenta a pagina principal quando o usuário esta logado"""
    if request.user.is_authenticated:
        id = request.user.id

        #queryset
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        # receitas = Receita.objects.filter(pessoa=id)
        # receitas = Receita.objects.filter(pessoa=request.user.id)
        
        #passando para o template renderizar só os dados que estao na queryset
        context = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', context)

    else:
        return redirect('home')

#refatorando
def campo_vazio(campo):
    """ valida campo vazio no cadastro """
    return not campo.strip()


def senhas_nao_iguais(senha, senha2):
    """ checa se senhas sao iguais na criacao de usuario"""
    return senha != senha2