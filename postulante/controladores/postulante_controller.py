from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from postulante.services.gestionar_postulante_servicio import GestionarPostulanteServicio
from django.http import JsonResponse

class PostulanteController(APIView):
    def post(self, request):
        servicio = GestionarPostulanteServicio()
        postulante = servicio.crear_postulante(request.data)
        return Response({
            "mensaje": "Postulante creado correctamente",
            "id": str(postulante.id)
        }, status=status.HTTP_201_CREATED)

def formulario_postulante(request):
    return JsonResponse({"mensaje": "Vista de formulario funcionando"})
