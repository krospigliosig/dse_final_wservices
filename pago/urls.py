from django.urls import path
from pago.controladores.pago_controller import PagoController

app_name = "pago"

urlpatterns = [
    path('verificar/', PagoController.as_view(), name="verificar_pago"),
]
