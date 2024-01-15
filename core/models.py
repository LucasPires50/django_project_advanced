import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from djmoney.models.fields import MoneyField
from stdimage.models import StdImageField


ICONE_CHOICES = {
    ('lni-cog', 'Engrenagem'),
    ('lni-stats-up', 'Gráfico'),
    ('lni-users', 'Usuários'),
    ('lni-layers', 'Design'),
    ('lni-mobile', 'Mobile'),
    ('lni-rocket', 'Foguete'),
    ('lni-laptop-phone', 'Celular'),
    ('lni-leaf', 'Folha'),
    ('lni-layers', 'Camadas'),
    ('lni-package', 'Caixa'),
    ('lni-drop', 'Gota'),
    ('lni-star', 'Estrela'),
}

def get_file_path(instance, filename):
    # mudar o nome dos arquivos salvos, para uma chave aleátoria
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    
    class Meta:
        abstract = True

class Servico(Base):
    servico = models.CharField('Cargo', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES)
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        
    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        
    def __str__(self):
        return self.cargo

class Equipe(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey("core.Cargo", verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=100)
    image = StdImageField('Imagens', upload_to=get_file_path, variations={'thumb': {'width':480, 'height':480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    
    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
        
    def __str__(self):
        return self.nome

class Recurso(Base):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=100)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
        
    def __str__(self):
        return self.nome
    
class Plano(Base):
    nome = models.CharField('Name', max_length=50)
    valor = MoneyField('Valor', max_digits=4, decimal_places=0, default_currency='BRL')
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES)
    numero_usuarios = models.CharField('Número de usuários', max_length=50)
    armazenamento = models.CharField('Armazenamento', max_length=50)
    tipo_suporte = models.CharField('Tipo de suporte', max_length=50)
    atualizacao = models.CharField('Atualização', max_length=50)

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'
        
    def __str__(self):
        return self.nome

class Depoimento(Base):
    image = StdImageField('Imagens', upload_to=get_file_path, variations={'thumb': {'width':480, 'height':480, 'crop': True}})
    nome = models.CharField('Name', max_length=50)
    cargo = models.ForeignKey("core.Cargo", verbose_name='Cargo', on_delete=models.CASCADE)
    depoimento = models.TextField('Descrição', max_length=100)
    nota = models.IntegerField('Nota', validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'
        
    def __str__(self):
        return self.nome
    
    