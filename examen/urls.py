from django.urls import path
from examen.controladores.examen_controller import ExamenController

app_name = "examen"

urlpatterns = [
    path('', ExamenController.as_view(), name="lista_examenes"),
]
