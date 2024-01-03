from typing import Any
from django.views.generic import TemplateView

from .models import Servico, Equipe, Recurso

class IndexView(TemplateView):
    template_name = "index.html"
    
    # Metodo para recuperar o context da pagina "index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # Adiconar novas informações ao context
        context['servicos'] = Servico.objects.order_by('?').all() # Vai ordenar por qualquer campo de forma aleátoria 
        context['equipes'] = Equipe.objects.order_by('?').all()
        context['recursos'] = Recurso.objects.order_by('?').all()
        
        return context
        

class TestView(TemplateView):
    template_name = "500.html"