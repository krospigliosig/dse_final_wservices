from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser 
from postulante.services.gestionar_postulante_servicio import GestionarPostulanteServicio


class PostulanteController(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        servicio = GestionarPostulanteServicio()
        datos = {
            "nombres": request.data.get("nombres"),
            "apellidos": request.data.get("apellidos"),
            "dni": request.data.get("dni"),
            "email": request.data.get("email")
        }
        archivo_documento = request.FILES.get("archivo_documento")
        postulante = servicio.crear_postulante(datos, archivo_documento)
        return Response({
            "mensaje": "Postulante creado ",
            "id": str(postulante.id),
            "dni": postulante.dni,
        }, status=status.HTTP_201_CREATED)
