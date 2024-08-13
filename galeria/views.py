'''Módulo para views da galeria Django.'''
from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    '''Responde à request para a página inicial da galeria.'''
    fotografias = Fotografia.objects.order_by("-id").filter(publicado=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    '''Responde à request para a página de imagem da galeria.'''
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    '''Responde à request para a página com filtro de busca.'''
    fotografias = Fotografia.objects.order_by("-id").filter(publicado=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {'cards': fotografias})