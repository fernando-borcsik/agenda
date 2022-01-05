from django.shortcuts import render, redirect, HttpResponse
from core.models import Evento
# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

def evento(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('<h1>O local do evento "{}" do usuário "{}" é: {}</h1>'.format(evento.titulo, evento.usuario, evento.local))
