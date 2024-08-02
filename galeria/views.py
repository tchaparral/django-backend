from django.shortcuts import render


def index(request):
    '''resposta da request'''
    return render(request, 'galeria/index.html')

def imagem(request):
    '''resposta imagem'''
    return render(request, 'galeria/imagem.html')