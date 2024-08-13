'''Importa o módulo de modelos do Django para definir modelos de banco de dados'''
from django.db import models

from datetime import datetime


class Fotografia(models.Model):
    '''Modelo que representa uma fotografia.'''

    OPCOES_DE_CATEGORIA = [
        ('Nebulosa', 'Nebulosa'),
        ('Estrela', 'Estrela'),
        ('Galaxia', 'Galaxia'),
        ('Planeta', 'Planeta')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_DE_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicado = models.BooleanField(default=False)
    data_log = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'Fotografia id={self.id}, nome={self.nome}'
