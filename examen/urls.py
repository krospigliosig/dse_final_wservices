from django.urls import path
from examen.controladores.examen_controller import ExamenController

urlpatterns = [
    path("registrar/", ExamenController.as_view())
]
