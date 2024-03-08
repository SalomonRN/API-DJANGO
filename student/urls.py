from rest_framework import routers
from .views import estudiante_detail, estudiante_all
from django.urls import path, include

router = routers.DefaultRouter()

# router.register("api/Estudiante", EstudianteViewSet, "Estudiante")

urlpatterns = [
    path("api/estudi/", estudiante_all),
    path("api/estudi/<int:id>", estudiante_detail), 
    
    ]
