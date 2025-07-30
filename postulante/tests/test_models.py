from django.test import TestCase
from postulante.infraestructura.models.postulante_model import PostulanteModel
from datetime import date

class PostulanteModelTest(TestCase):
    def test_crear_postulante_valido(self):
        postulante = PostulanteModel.objects.create(
            nombres="Salim",
            apellidos="Jorge",
            dni="12345678",
            email="salim@example.com",
            fecha_nacimiento=date(2000, 1, 1),
            estado="activo"
        )
        self.assertEqual(postulante.nombres, "Salim")
        self.assertEqual(postulante.estado, "activo")
