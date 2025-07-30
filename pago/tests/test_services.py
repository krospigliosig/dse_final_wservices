from django.test import TestCase
from pago.services.procesar_pago_servicio import ProcesarPagoServicio
from postulante.infraestructura.models.postulante_model import PostulanteModel

class ProcesarPagoServiceTest(TestCase):
    def test_pago_exitoso(self):
        # Crear postulante simulado
        postulante = PostulanteModel.objects.create(
            nombres="Juan",
            apellidos="Ramos",
            dni="87654321",
            email="juan@example.com",
            fecha_nacimiento="2001-01-01",
            estado="activo"
        )

        datos = {
            "postulante_id": postulante.id,
            "monto": 200.0,
            "moneda": "PEN"
        }

        servicio = ProcesarPagoServicio()
        pago = servicio.registrar_pago(datos)

        self.assertEqual(pago.monto, 200.0)
        self.assertEqual(pago.estado, "PENDIENTE")
        self.assertEqual(pago.moneda, "PEN")
