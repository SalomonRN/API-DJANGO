from rest_framework import serializers
from .models import Estudiante


class EstudianteSerializer( ):
    class Meta:
        model = Estudiante
        fields = '__all__'