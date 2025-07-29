from pago.repositories.interface.pago_repositorio import IPagoRepositorio
from pago.domain.pago import Pago
from pago.domain.transaccion_bancaria import TransaccionBancaria
from pago.infraestructura.models.pago_model import PagoModel
from pago.infraestructura.models.transaccion_bancaria_model import TransaccionBancariaModel
from postulante.infraestructura.models.postulante_model import PostulanteModel
from uuid import UUID

class PagoRepositorioImpl(IPagoRepositorio):
    def guardar(self, pago: Pago) -> None:
        transaccion_model = None
        if pago.transaccion:
            transaccion_model, _ = TransaccionBancariaModel.objects.get_or_create(
                id_transaccion=pago.transaccion.id_transaccion,
                defaults={
                    "fecha": pago.transaccion.fecha,
                    "banco": pago.transaccion.banco,
                    "monto": pago.transaccion.monto
                }
            )

        PagoModel.objects.update_or_create(
            id=pago.id,
            defaults={
                "postulante": PostulanteModel.objects.get(id=pago.postulante_id),
                "monto": pago.monto,
                "moneda": pago.moneda,
                "estado": pago.estado,
                "motivo_rechazo": pago.motivo_rechazo,
                "transaccion": transaccion_model
            }
        )

    def obtener_por_id(self, id: UUID) -> Pago:
        modelo = PagoModel.objects.get(id=id)
        transaccion = None
        if modelo.transaccion:
            transaccion = TransaccionBancaria(
                id_transaccion=modelo.transaccion.id_transaccion,
                fecha=modelo.transaccion.fecha,
                banco=modelo.transaccion.banco,
                monto=modelo.transaccion.monto
            )
        return Pago(
            id=modelo.id,
            postulante_id=modelo.postulante.id,
            monto=modelo.monto,
            moneda=modelo.moneda,
            fecha_creacion=modelo.fecha_creacion,
            estado=modelo.estado,
            motivo_rechazo=modelo.motivo_rechazo,
            transaccion=transaccion
        )