from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import CategoriaIncidencia, Incidencia, HistorialEstado
from .serializers import (
    UserSerializer,
    CategoriaIncidenciaSerializer,
    IncidenciaSerializer,
    HistorialEstadoSerializer
)

# Create your views here.

def index_view(request):
    return render(request, 'sist_urb/index.html')

def error_404_view(request, exception):
    return render(request, 'sist_urb/404.html', status=404)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoriaIncidenciaViewSet(viewsets.ModelViewSet):
    queryset = CategoriaIncidencia.objects.all()
    serializer_class = CategoriaIncidenciaSerializer


class IncidenciaViewSet(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer


class HistorialEstadoViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstado.objects.all()
    serializer_class = HistorialEstadoSerializer