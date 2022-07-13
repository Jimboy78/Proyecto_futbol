from django.views.generic.list import ListView
from django.views.generic import  DetailView
from .models import Equipo

# Create your views here.

class TablaDeEquipos(ListView):

    model = Equipo
    template_name = 'tabla_equipos/templates/tabla_de_equipos.html'

class DetalleEquipo(DetailView):
    model = Equipo
    template_name = 'tabla_equipos/templates/detalle_equipo.html'
    
 