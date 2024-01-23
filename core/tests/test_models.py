import uuid
from django.test import TestCase
from model_bakery import baker
from moneyed import Money

from core.models import get_file_path


class GetFilePathTestCase(TestCase):
    
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'
    
    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))

class ServicoTestCase(TestCase):
    
    def setUp(self):
        self.servico = baker.make('Servico')
    
    def test_str(self):
        self.assertEqual(str(self.servico), self.servico.servico)

class CargoTestCase(TestCase):
    
    def setUp(self):
        self.cargo = baker.make('Cargo')
    
    def test_str(self):
        self.assertEqual(str(self.cargo), self.cargo.cargo)

class EquipeTestCase(TestCase):
    
    def setUp(self):
        self.equipe = baker.make('Equipe')
    
    def test_str(self):
        self.assertEqual(str(self.equipe), self.equipe.nome)                  

class RecursoTestCase(TestCase):
    
    def setUp(self):
        self.recurso = baker.make('Recurso')
    
    def test_str(self):
        self.assertEqual(str(self.recurso), self.recurso.nome)

class PlanoTestCase(TestCase):
    
    def setUp(self):
        self.plano = baker.make('Plano', valor=Money(100, 'BRL'))
    
    def test_str(self):
        self.assertEqual(str(self.plano), self.plano.nome) 

class DepoimentoTestCase(TestCase):
    
    def setUp(self):
        self.depoimento = baker.make('Depoimento')
    
    def test_str(self):
        self.assertEqual(str(self.depoimento), self.depoimento.nome) 
