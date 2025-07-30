from pago.domain.pago import Pago

class ServicioPago:
    @staticmethod
    def procesar_pago(dni: str, monto: float, servicio: str) -> Pago:
        if monto >= 60:
            estado = "aprobado"
        else:
            estado = "rechazado"
        
        return Pago(
            dni=dni,
            monto=monto,
            servicio=servicio,
            estado_transaccion=estado
        )
