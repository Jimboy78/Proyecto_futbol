from django.views.generic.list import ListView
from .models import Equipo

# Create your views here.

class TablaDeEquipos(ListView):

    model = Equipo
    template_name = 'tabla_equipos/templates/tabla_de_equipos.html'