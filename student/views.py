from .models import Estudiante
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import EstudianteSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EstudianteSerializer
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def estudiante_detail(request, id):
    try:
        estudiante = Estudiante.objects.filter(id=id)
    except Estudiante.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(EstudianteSerializer(estudiante))

    elif request.method == 'PUT':
        serializer = EstudianteSerializer(estudiante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        estudiante.delete()
        return Response(data="ELIMINADO", status=status.HTTP_204_NO_CONTENT)
    
# from student.models import Estudiante