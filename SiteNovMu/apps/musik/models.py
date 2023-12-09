from django.db import models
from django.test import TestCase

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField('Nome', max_lenght=100)
    idade =  models.PositiveIntegerField('Idade')

    def __str__(self):
        return self.nome
# BANCO DE DADOS TEM DE TER PERMISSÃO PARA CRIAR 
# NOVOS BANCOS POIS OS BANCOS CRIADOS NO MKMIGRATIONS 
# SÃO TEMPORÁRIOS
