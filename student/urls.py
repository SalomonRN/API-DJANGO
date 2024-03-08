from rest_framework import routers
from .views import EstudianteViewSet
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()

router.register(r'api/Estudiante', EstudianteViewSet, 'Estudiante')

urlpatterns = [
    path("", include(router.urls)), 
    path("docs/", include_docs_urls(title="EST"))
]
