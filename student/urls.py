from rest_framework import routers
from .views import EstudianteViewSet

router = routers.DefaultRouter()

router.register(r'api/Estudiante', EstudianteViewSet, 'Estudiante')

urlpatterns = router.urls