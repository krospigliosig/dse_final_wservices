from django.test import TestCase, Client
from django.urls import reverse

class PostulanteViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_formulario_postulante(self):
        response = self.client.get(reverse("postulante:formulario"))  # Ajusta nombre
        self.assertEqual(response.status_code, 200)
