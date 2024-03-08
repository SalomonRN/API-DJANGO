from .models import Estudiante
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import EstudianteSerializer


@api_view(["GET", "POST"])
def estudiante_all(request):
    if request.method == "GET":
        estudiantes = Estudiante.objects.all()
        estudiantes_serialize = EstudianteSerializer(estudiantes, many=True)
        return Response(estudiantes_serialize.data)

    elif request.method == "POST":
        estudiante_serialize = EstudianteSerializer(data=request.data)
        if estudiante_serialize.is_valid():
            estudiante_serialize.save()
            return Response(data=["ESTUDIANTE CREADO", estudiante_serialize.data])
        return Response(data=["ESTUDIANTE NO CREADO", estudiante_serialize.errors])


@api_view(["GET", "PUT", "DELETE"])
def estudiante_detail(request, id):
    try:
        estudiante = Estudiante.objects.get(id=id)
    except Estudiante.DoesNotExist:
        return Response(data="NO EXISTE NINGUN USUARIO CON ESE ID", status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(
            EstudianteSerializer(estudiante).data, status=status.HTTP_200_OK
        )

    elif request.method == "PUT":
        serializer = EstudianteSerializer(estudiante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        estudiante.delete()
        return Response(data="ESTUDIANTE ELIMINADO CORRECTAMENTE", status=status.HTTP_204_NO_CONTENT)


# from student.models import Estudiante
