from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio.as_view(), name="inicio"),
    path('equipos/', views.Equipos.as_view(), name="equipos"),
    path('acerca_de/', views.AcercaDe.as_view(), name="acerca_de"),
    path('contacto/', views.Contacto.as_view(), name="contacto"),
]
