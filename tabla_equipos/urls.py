from django.urls import path
from . import views

urlpatterns = [

    path('equipos/tabla_de_equipos', views.TablaDeEquipos.as_view(), name="tabla_de_equipos"),
]
