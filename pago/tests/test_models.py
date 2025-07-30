from django.test import TestCase
from pago.infraestructura.models.pago_model import PagoModel
from postulante.infraestructura.models.postulante_model import PostulanteModel

class PagoModelTest(TestCase):
    def test_crear_pago(self):
        postulante = PostulanteModel.objects.create(
            nombres="Salim",
            apellidos="Jorge",
            dni="12345678",
            email="salim@example.com",
            fecha_nacimiento="2000-01-01",
            estado="activo"
        )

        pago = PagoModel.objects.create(
            postulante=postulante,
            monto=150.0,
            moneda="PEN",
            estado="APROBADO"
        )

        self.assertEqual(pago.monto, 150.0)
        self.assertEqual(pago.moneda, "PEN")
        self.assertEqual(pago.estado, "APROBADO")
        self.assertEqual(str(pago.postulante.dni), "12345678")
