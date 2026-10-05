from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CategoriaIncidencia, Incidencia, HistorialEstado

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class CategoriaIncidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaIncidencia
        fields = '__all__'


class IncidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidencia
        fields = '__all__'


class HistorialEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEstado
        fields = '__all__'