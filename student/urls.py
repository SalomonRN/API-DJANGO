from rest_framework import routers
from .views import EstudianteViewSet, estudiante_detail
from django.urls import path, include

router = routers.DefaultRouter()

router.register("api/Estudiante", EstudianteViewSet, "Estudiante")

urlpatterns = [path("api/estudi/<int:id>", estudiante_detail)]
