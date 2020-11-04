from django.shortcuts import render, redirect
# import datetime

from .forms import TransacaoForm
# from django.http import HttpResponse
from .models import Transacao


def home(request):
    # now  = datetime.datetime.now()
    # html = "<html><body> It is now %s.</body><hml>" % now
    # return HttpResponse(html)
    return render(request, 'contas/home.html')

def listagem(request):  
    data = {}
    data['transacoes'] = Transacao.objects.all() #busca todas as Transações/objects é um manager
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)#O Django verifica se há algo preenchido no form, se tiver ele cria um form com as informações preenchidas.
    #Verificar se o form é válido antes de salvar no BD
    if form.is_valid():
        form.save()
        return redirect('url_listagem')#Mandar pra onde eu desejo
    data['form'] = form
    return render(request, 'contas/form.html', data)

def update(request, pk):#pk = primarykey
    data = {}
    #Pegar a transação do BD, pra poder fazer o update.
    transacao = Transacao.objects.get(pk=pk)#vai localizar essa transação no banco e vai criar um objeto chamado transacao.
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['transacao'] = transacao 
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')