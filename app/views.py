from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.
def lembrei(request): 
    return render(request, 'primeiro.html')


def ver(request):
    pessoas = {
        'pessoas': Pessoa.objects.all()
    }
    return render(request, 'ver.html', pessoas)


def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'cadastrar.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        pessoa = Pessoa(nome=nome, idade=idade, email=email, telefone=telefone)
        cadastrados = Pessoa.objects.filter(email=email)
        if cadastrados.exists():
            print('Usuário já existe')
        else:
            pessoa.save()
            print('\033[1;32mDados cadastrados\033[m')
        return render(request, 'cadastrar.html')


def atualizar(request, pk):
    if request.method == 'GET':
        cadastro = Pessoa.objects.get(id=pk)
        return render(request, 'atualizar.html', {'pessoa': cadastro})
    elif request.method == 'POST':
        try:
           new_nome = request.POST.get('nome')
           new_idade = request.POST.get('idade')
           new_email = request.POST.get('email')
           new_telefone = request.POST.get('telefone')

           cadastro = Pessoa.objects.get(id=pk)

           cadastro.nome = new_nome
           cadastro.idade = new_idade
           cadastro.email = new_email
           cadastro.telefone = new_telefone

           cadastro.save()
           return redirect('ver')
        except Pessoa.DoesNotExist:
            print('não existe')
            return render(request, 'atualizar.html')
        

def deletar(request):
    if request.method == 'GET':
        return render(request, 'deletar.html')
    elif request.method == 'POST':
        try:
            id = request.POST.get('id')
            pessoa = Pessoa.objects.get(id=id)
            pessoa.delete()
            return redirect('/')     
        except Pessoa.DoesNotExist:
             print('Usuário não encontrado!')
        
        return render(request, 'deletar.html')
