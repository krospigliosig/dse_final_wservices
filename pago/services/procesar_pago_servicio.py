from uuid import uuid4
from datetime import datetime
from pago.domain.pago import Pago
from pago.repositories.implementacion.pago_repositorio_impl import PagoRepositorioImpl

class ProcesarPagoServicio:
    def __init__(self):
        self.repositorio = PagoRepositorioImpl()

    def registrar_pago(self, datos: dict) -> Pago:
        pago = Pago(
            id=uuid4(),
            postulante_id=datos["postulante_id"],
            monto=datos["monto"],
            moneda=datos["moneda"],
            fecha_creacion=datetime.now(),
            estado="PENDIENTE"
        )
        self.repositorio.guardar(pago)
        return pago

    def aprobar_pago(self, id_pago):
        pago = self.repositorio.obtener_por_id(id_pago)
        pago.aprobar()
        self.repositorio.guardar(pago)

    def rechazar_pago(self, id_pago, motivo: str):
        pago = self.repositorio.obtener_por_id(id_pago)
        pago.rechazar(motivo)
        self.repositorio.guardar(pago)
