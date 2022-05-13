from django.shortcuts import render
from django.views.generic.base import TemplateView


class Inicio (TemplateView):
    template_name = 'Indice/templates/index.html'


    
class AcercaDe (TemplateView):
    template_name = 'Indice/templates/acerca_de.html'


    
class Equipos (TemplateView):
    template_name = 'Indice/templates/equipos.html'



class Contacto (TemplateView):
    template_name = 'Indice/templates/contacto.html'
    
