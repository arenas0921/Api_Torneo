from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class TorneoViewSet(viewsets.ModelViewSet):
    queryset = Torneo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TorneoSerializer


class FechaViewSet(viewsets.ModelViewSet):
    queryset = Fecha.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FechaSerializer


class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PartidoSerializer


class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EquipoSerializer


class Partido_EquipoViewSet(viewsets.ModelViewSet):
    queryset = Partido_Equipo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Partido_EquipoSerializer


class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Judador.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JugadorSerializer


class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TecnicoSerializer
