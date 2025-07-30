from django.test import TestCase
from examen.infraestructura.models.examen_model import ExamenModel
from postulante.infraestructura.models.postulante_model import PostulanteModel
from datetime import datetime, date

class ExamenModelTest(TestCase):
    def test_creacion_examen(self):
        postulante = PostulanteModel.objects.create(
            nombres="Salim",
            apellidos="Jorge",
            dni="12345678",
            email="salim@example.com",
            fecha_nacimiento=date(2003, 3, 16),
            estado="activo"
        )

        examen = ExamenModel.objects.create(
            postulante=postulante,
            fecha=datetime.now(),
            estado="PROGRAMADO",
            resultado_puntaje=90.0,
            resultado_aprobado=True,
            resultado_comentario="Buen desempeño",
            resultado_fecha_publicacion=datetime.now()
        )


        self.assertEqual(examen.estado, "PROGRAMADO")
