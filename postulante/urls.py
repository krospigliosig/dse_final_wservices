from django.urls import path
from postulante.controladores.postulante_controller import PostulanteController

urlpatterns = [
    path('', PostulanteController.as_view()), 
]
