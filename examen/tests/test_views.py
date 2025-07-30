from django.test import TestCase
from django.urls import reverse
from postulante.infraestructura.models.postulante_model import PostulanteModel
from pago.infraestructura.models.pago_model import PagoModel
from datetime import date
import json

class ExamenViewsTest(TestCase):
    def setUp(self):
        # Crear postulante
        self.postulante = PostulanteModel.objects.create(
            nombres="Salim",
            apellidos="Jorge",
            dni="12345678",
            email="salim@example.com",
            fecha_nacimiento=date(2003, 3, 16),
            estado="activo"
        )

        # Crear pago aprobado
        PagoModel.objects.create(
            postulante=self.postulante,
            monto=150.0,
            moneda="PEN",
            estado="APROBADO"
        )

    def test_registro_examen_post(self):
        response = self.client.post(
        reverse("examen:lista_examenes"),
        data=json.dumps({
            "dni": "12345678",
            "puntaje": 90,
            "comentario": "Buen desempeño"
        }),
        content_type="application/json"
)

        print(">>> RESPONSE JSON:", response.json())  

        self.assertEqual(response.status_code, 201)

