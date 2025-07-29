from datetime import datetime

class TransaccionBancaria:
    def __init__(self, id_transaccion: str, fecha: datetime, banco: str, monto: float):
        self.id_transaccion = id_transaccion
        self.fecha = fecha
        self.banco = banco
        self.monto = monto