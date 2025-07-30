from django.urls import path
from pago.controladores.pago_controller import RegistrarPagoAPI

urlpatterns = [
    path('', RegistrarPagoAPI.as_view(), name='registrar_pago'),
]
