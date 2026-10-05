from django.urls import path
from . import views
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    CategoriaIncidenciaViewSet,
    IncidenciaViewSet,
    HistorialEstadoViewSet
)

urlpatterns = [
    path('', views.index_view, name='index'),
]



router = DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'categorias', CategoriaIncidenciaViewSet)
router.register(r'incidencias', IncidenciaViewSet)
router.register(r'historial-estados', HistorialEstadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]