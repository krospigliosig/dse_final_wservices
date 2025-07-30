from django.test import TestCase
from postulante.services.registrar_postulante_servicio import registrar_postulante
from datetime import date

class RegistrarPostulanteServiceTest(TestCase):
    def test_registro_valido(self):
        data = {
            "nombres": "Salim",
            "apellidos": "Jorge",
            "dni": "12345678",
            "email": "salim@example.com",
            "fecha_nacimiento": date(2000, 1, 1),
            "estado": "activo"
        }
        postulante = registrar_postulante(data)
        self.assertEqual(postulante.estado, "activo")
