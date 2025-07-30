from django.urls import path
from postulante.controladores.postulante_controller import formulario_postulante

app_name = "postulante"

urlpatterns = [
    path("formulario/", formulario_postulante, name="formulario"),
]
