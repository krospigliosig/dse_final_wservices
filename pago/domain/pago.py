
class Pago:
    def __init__(self, dni: str, monto: float, servicio: str, estado_transaccion: str,):
        self.dni = dni
        self.monto = monto
        self.servicio = servicio
        self.estado_transaccion = estado_transaccion
