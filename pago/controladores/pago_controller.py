from pago.services.procesar_pago_servicio import ServicioPago
from pago.repositories.implementacion.pago_repositorio_impl import PagoRepositorioImpl
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegistrarPagoAPI(APIView):
    def post(self, request):
        try:
            dni = request.data.get("dni")
            monto = float(request.data.get("montoTotal"))
            servicio = request.data.get("servicio")
            pago = ServicioPago.procesar_pago(dni, monto, servicio)
            repositorio = PagoRepositorioImpl()
            repositorio.guardar_pago(pago)

            return Response({
                "mensaje": "Pago procesado ",
                "estado": pago.estado_transaccion
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
