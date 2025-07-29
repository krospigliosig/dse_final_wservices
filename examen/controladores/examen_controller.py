from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from examen.repositories.implementacion.examen_repositorio_impl import ExamenRepositorioImpl
from examen.services.registrar_examen_servicio import RegistrarExamenServicio

class ExamenController(APIView):
    def post(self, request):
        try:
            dni = request.data["dni"]
            puntaje = float(request.data["puntaje"])
            comentario = request.data.get("comentario", "")

            servicio = RegistrarExamenServicio(ExamenRepositorioImpl())
            servicio.ejecutar(dni, puntaje, comentario)

            return Response({"mensaje": "Examen registrado correctamente"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
