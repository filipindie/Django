from django.shortcuts import render
# from django.http import HttpResponse
from .models import Transacao
import datetime

def home(request):
    # now  = datetime.datetime.now()
    # html = "<html><body> It is now %s.</body><hml>" % now
    # return HttpResponse(html)
    return render(request, 'contas/home.html')

def listagem(request):  
    data = {}
    data['transacoes'] = Transacao.objects.all() #busca todas as Transações/objects é um manager
    return render(request, 'contas/listagem.html', data)