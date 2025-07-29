# pago/urls.py
from django.urls import path
from pago.controladores.pago_controller import PagoController

urlpatterns = [
    path('', PagoController.as_view(), name='crear_pago'),
]
