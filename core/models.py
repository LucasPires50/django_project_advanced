import uuid
from django.db import models
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