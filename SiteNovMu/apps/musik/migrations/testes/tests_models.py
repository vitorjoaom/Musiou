from django.test import TestCase
from models import Pessoa
# Create your tests here.

class PessoaTestCase(TestCase):

    def setUp(self):
        Pessoa.objects.create(
            nome="Francisco André",
            idade=38
        )
# SEMPRE SERÁ NECESSÁRIO COLOCAR O NOME
# TEST ANTES DAS FUNÇÕES DE TESTE    
    def test_retorno_str(self):
        p1 = Pessoa.objects.get(nome='João André')
        self.assertEquals(p1.__str__(), 'João André')