from django.test import TestCase
from django.urls import reverse
import json
from postulante.infraestructura.models.postulante_model import PostulanteModel

class PagoViewsTest(TestCase):
    def test_validar_pago_view(self):
        postulante = PostulanteModel.objects.create(
            nombres="Salim",
            apellidos="Jorge",
            dni="12345678",
            email="salim@example.com",
            fecha_nacimiento="2000-01-01",
            estado="activo"
        )

        data = {
            "postulante": str(postulante.id),
            "monto": 150.0,
            "moneda": "PEN",
            "transaccion": {
                "id_transaccion": "TRX123456",
                "fecha": "2025-07-30T10:00:00",
                "banco": "Interbank",
                "monto": 150.0
            }
        }

        response = self.client.post(
            reverse("pago:verificar_pago"),  # Asegúrate que esta ruta exista en tu urls.py
            data=json.dumps(data),
            content_type="application/json"
        )

        print(">>> RESPONSE JSON:", response.json())
        self.assertEqual(response.status_code, 201)
