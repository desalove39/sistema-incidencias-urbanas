from django.db import models
from django.contrib.auth.models import User

class CategoriaIncidencia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Incidencia(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En Proceso'),
        ('RESUELTO', 'Resuelto'),
        ('RECHAZADO', 'Rechazado'),
    ]

    PRIORIDAD_CHOICES = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
        ('CRITICA', 'Crítica'),
    ]

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=255)
    categoria = models.ForeignKey(CategoriaIncidencia, on_delete=models.CASCADE, related_name='incidencias')
    ciudadano = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidencias_reportadas')
    tecnico_asignado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='incidencias_asignadas')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD_CHOICES, default='MEDIA')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} - {self.get_estado_display()}"


class HistorialEstado(models.Model):
    incidencia = models.ForeignKey(Incidencia, on_delete=models.CASCADE, related_name='historial_estados')
    estado_anterior = models.CharField(max_length=20)
    estado_nuevo = models.CharField(max_length=20)
    modificado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comentario = models.TextField(blank=True, null=True)
    fecha_cambio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Incidencia #{self.incidencia.id}: {self.estado_anterior} -> {self.estado_nuevo}"