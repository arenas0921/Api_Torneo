from rest_framework import serializers
from .models import *


class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = "__all__"


class FechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fecha
        fields = "__all__"


class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = "__all__"


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = "__all__"


class Partido_EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = "__all__"


class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judador
        fields = "__all__"


class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = "__all__"
