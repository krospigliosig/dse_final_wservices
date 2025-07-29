# pago/controladores/pago_controller.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid
from pago.infraestructura.models.pago_model import PagoModel
from pago.infraestructura.models.transaccion_bancaria_model import TransaccionBancariaModel
from postulante.infraestructura.models.postulante_model import PostulanteModel  
from datetime import datetime



class PagoController(APIView):
    def post(self, request):
        try:
            data = request.data
            postulante = PostulanteModel.objects.get(id=data['postulante'])
            fecha = datetime.fromisoformat(data['transaccion']['fecha']) 
            transaccion = TransaccionBancariaModel.objects.create(
                id_transaccion=data['transaccion']['id_transaccion'],
                fecha=fecha,
                banco=data['transaccion']['banco'],
                monto=data['transaccion']['monto']
            )

            pago = PagoModel.objects.create(
                id=uuid.uuid4(),
                postulante=postulante,
                monto=data['monto'],
                moneda=data['moneda'],
                estado='PENDIENTE',
                transaccion=transaccion
            )

            return Response({
                "mensaje": "Pago registrado correctamente",
                "pago_id": str(pago.id),
                "estado": pago.estado
            }, status=status.HTTP_201_CREATED)

        except PostulanteModel.DoesNotExist:
            return Response({"error": "Postulante no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
