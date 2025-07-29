from uuid import UUID
from datetime import datetime
from .transaccion_bancaria import TransaccionBancaria

class Pago:
    def __init__(self, id: UUID, postulante_id: UUID, monto: float, moneda: str,
                 fecha_creacion: datetime, estado: str,
                 transaccion: TransaccionBancaria = None, motivo_rechazo: str = ""):
        self.id = id
        self.postulante_id = postulante_id
        self.monto = monto
        self.moneda = moneda
        self.fecha_creacion = fecha_creacion
        self.estado = estado
        self.transaccion = transaccion
        self.motivo_rechazo = motivo_rechazo

    def aprobar(self):
        self.estado = "APROBADO"
        self.motivo_rechazo = ""

    def rechazar(self, motivo: str):
        self.estado = "RECHAZADO"
        self.motivo_rechazo = motivo

    def es_aprobado(self):
        return self.estado == "APROBADO"
