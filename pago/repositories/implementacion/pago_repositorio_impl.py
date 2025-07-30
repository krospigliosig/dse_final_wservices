from pago.repositories.interface.pago_repositorio import PagoRepositorio
from pago.domain.pago import Pago
from pago.infraestructura.models.pago_model import PagoModel

class PagoRepositorioImpl(PagoRepositorio):

    def guardar_pago(self, pago: Pago):
        PagoModel.objects.create(
            dni=pago.dni,
            monto=pago.monto,
            servicio=pago.servicio,
            estado_transaccion=pago.estado_transaccion
        )

    def obtener_pagos_por_dni(self, dni: str) -> list[Pago]:
        pagos_model = PagoModel.objects.filter(dni=dni)
        return [
            Pago(
                dni=p.dni,
                monto=p.monto,
                servicio=p.servicio,
                estado_transaccion=p.estado_transaccion
            )
            for p in pagos_model
        ]
