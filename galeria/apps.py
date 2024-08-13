'''Configura a aplicação 'Galeria' no Django'''
from django.apps import AppConfig


class GaleriaConfig(AppConfig):
    '''Configuração da aplicação 'Galeria'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'galeria'
